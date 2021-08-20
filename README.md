# Anaconda商用利用有償化対策

Anacondaの商用利用が有償化された（2020/04/10現在）．以下[Anaconda パッケージリポジトリが「大規模な」商用利用では有償になっていた](https://qiita.com/tfukumori/items/f8fc2c53077b234384fc)より．

> | 区分 | 条件                                                         |
> | ---- | ------------------------------------------------------------ |
> | 無償 | ・個人が個人的な非ビジネス目的で使用する<br/>・教育機関の学生または職員が教育活動に関連して使用する<br/>・慈善サービスの提供に関連して、非営利団体の従業員やボランティアが使用する、または<br/> ・従業員の総数が200人未満の共通支配下にある事業体（企業？）（[規約](https://www.anaconda.com/terms-of-service)では[entities](http://www.takahashi-office.jp/column/houritsu-keiyakusho/18.htm)と記載）が使用する |
> | 有償 | "無償"に記載した以外の条件でリポジトリを使用する場合         |

対策として，以下の２通りが候補として挙げられる．

|               |              メリット              | デメリット |
| :-----------: | -------------------------------- | -------- |
| [Miniconda+Pip](#minicondapip移行方法) | ・Anacondaと似たような使い方ができる | ・母体が同じなので，Anaconda同様商用利用有償化もありうる<br />・Anacondaほど扱っているパッケージが少ないので，結局Pipを使わないといけない<br/>＝パッケージ間のバージョンの競合の可能性は残る |
|  [Pyenv＋Venv+Pip](#pyenvvenvpip移行方法)  | ・MITライセンスなので，有償化の心配は上記より少なそう<br />・プロジェクトファイル内に`.venv`をおけるので，管理が楽 | ・移行作業が少し大変<br />・パッケージ間のバージョンの競合しやすくなる<br />・全て手動で管理（ある意味メリット） |

## 移行する前に

### パッケージ情報の出力

まず，移行する前に仮想環境上のパッケージ情報を出力させる．

- 面倒な方→[プログラム](https://github.com/jjjkkkjjj-mizuno/alt-anaconda/blob/master/createminienv.py)を作りました．（動作保証はしません）

  →直下に`{env}.yml`と`{env}.txt`が作成されます．

  ```bash
  python exportenv.py
  ```

- Miniconda+Pip用

  ```bash
  conda activate {hoge}
  conda env export > environment.yml
  ```

- Pyenv+Pip用

  ```bash
  conda install pip
  pip list --format=freeze > requirements.txt
  ```

### Anacondaアンインストール

- Windowsの場合
  Anacondaをインストールしている場所＞`Uninstall-Anaconda3.exe`実行

- Unixの場合

  ```bash
  rm -rf ~/anaconda3 # 適切なパス指定
  
  ```

## Miniconda＋Pip移行方法

### Minicondaインストール

- Windows
  [公式サイト](https://docs.conda.io/en/latest/miniconda.html)から`.exe`をダウンロードして実行

  - インストールが完了すると，以下のようにAnaconda Promptがminicondaに変わる

  ![image](https://user-images.githubusercontent.com/16914891/110093609-40e6a080-7dde-11eb-8a15-b87ff375ec6d.png)

- Unix(Linux or Mac)

  必要なバージョンを[公式サイト](https://docs.conda.io/en/latest/miniconda.html)や[バージョン履歴](https://repo.anaconda.com/miniconda/)から選ぶ

  ```bash
  sudo /bin/bash ~/miniconda.sh # -p /opt/conda # 場所を指定する場合
  rm ~/anaconda.sh
  
  source ~/.bashrc
  ```

### 移行作業

Anaconda Promptを起動する．

- `defaults`チャネルを削除し，`conda-forge`チャンネルを追加する．

  ```bash
  conda config --remove channels defaults 
  conda config --add channels conda-forge
  ```

- 先ほど作成した`yml`ファイルから仮想環境を作成

  ```bash
  conda env create -f {}.yml
  ```

- ↑が面倒な方→[プログラム](https://github.com/jjjkkkjjj-mizuno/alt-anaconda/blob/master/exportenvs.py)を作成しました．（例によって，動作保証はしません）

  ```bash
  python createminienv.py
  ```

https://qiita.com/kimisyo/items/986802ea52974b92df27

※Pipで`ValueError: check_hostname requires server_hostname`と出る場合（永続化する場合は，以下の変数を登録する必要がある）

- Windows

```
set HTTP_PROXY=http://user:pass@hostname:port
```

- Unix

```
export HTTP_PROXY="http://user:pass@hostname:port"
```

### 仮想環境作成

Anaconda Promptを起動する．

- 仮想環境を作成する（`{hoge}`は任意，`x.x`も任意のバージョン）

  ```bash
  conda create -n {hoge} python=x.x
  ```

- その仮想環境に入る

  ```bash
  conda activate {hoge}
  
  ## 以下のように左側に(hoge)と表示され，仮想環境に入ったことを表すようになる
  (hoge) $
  ```

  - 上記の状態で，必要なライブラリをインストール

    ```bash
    conda install {package}
    ```

  - `conda install`が失敗する場合は，`pip`でインストール

    ```bash
    pip install {package}
    ```

- 仮想環境から抜ける

  ```bash
  conda deactivate
  ```

### Jupyter Notebookを使いたい場合

Anaconda Promptを起動する．

- `base`環境にJupyterをインストールする

  ```bash
  conda install jupyter notebook
  ```

- 仮想環境に入って，kernelを追加する

  ```bash
  conda activate {hoge}
  
  #(hoge) $ のようになる
  conda install notebook ipykernel
  ipython kernel install --user --display-name {hoge}
  ```

- **仮想環境に入った状態**で，Jupyterを起動する

  ```bash
  conda activate {hoge}
  
  #(hoge) $ のようになる
  jupyter notebook
  ```

  あとは，以下のようにNew > Notebook > {hoge}選べば，その環境でJupyterが使える．

  ![image](https://user-images.githubusercontent.com/63040751/130174245-6910a4aa-8779-4d88-b9f6-41ceb6278928.png)



## Pyenv＋Venv+Pip移行方法

### Pyenvのインストール

- Windows

  - Gitをインストール

    - exeのダウンロード
      [https://git-scm.com/downloads](https://git-scm.com/downloads)から.exeをダウンロード
      
      ![git_install_win1](https://user-images.githubusercontent.com/63040751/78861350-8d5f1a00-7a6f-11ea-8fbf-8e168f5fd377.png)
  
    - exeを実行
      以下の通りに進めていけばOK．
      
      ![git_install_win2](https://user-images.githubusercontent.com/63040751/78861353-8e904700-7a6f-11ea-9026-117f57471ed7.png)
      
      ![git_install_win3](https://user-images.githubusercontent.com/63040751/78861355-8fc17400-7a6f-11ea-9ab6-4fcfa1686993.png)
      
      ![git_install_win4](https://user-images.githubusercontent.com/63040751/78861358-905a0a80-7a6f-11ea-927e-57e492e734f7.png)
      
      ![git_install_win5](https://user-images.githubusercontent.com/63040751/78861362-905a0a80-7a6f-11ea-822d-fea428c95258.png)
      
      ![git_install_win6](https://user-images.githubusercontent.com/63040751/78861364-918b3780-7a6f-11ea-8aad-603f5bd2fc54.png)
      
      ![git_install_win7](https://user-images.githubusercontent.com/63040751/78861366-92bc6480-7a6f-11ea-9eba-2896c17dc3dc.png)
  
    - git bashを開く
  
      ![git_install_win](https://user-images.githubusercontent.com/63040751/78873021-20567f00-7a85-11ea-85fe-1727a946f9ce.png)
      
    - Gitがインストールできたか確認
  
    ```bash
    git version
    >> git version x.yy.z (Apple Git-nnn)とか出たらOK
    ```
  
  - Pyenv-winインストール
  
    [公式Github](https://github.com/pyenv-win/pyenv-win)から`pyenv-win`をインストール．※以降コマンドプロンプトではなく，**Git Bash**から以下実行．

    ```bash
    # git bashを開いて以下のコマンドを実行
    git clone https://github.com/pyenv-win/pyenv-win.git "$HOME/.pyenv"
    ```
  
    **PowerShell**を開き，環境変数のPATHを通す．

    ```bash
    [System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
    [System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
    [System.Environment]::SetEnvironmentVariable('path', $HOME + "\.pyenv\pyenv-win\bin;" + $HOME + "\.pyenv\pyenv-win\shims;" + $env:Path,"User")
    ```
  
    一度Git bashを閉じ，再度開いて以下のコマンドで，Pyenvのバージョンが表示されればOK.

    ```bash
    pyenv --version 
    # pyenv 2.64.3
    ```
  
- Unix

  ```bash
  cd ~
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```
  
  - Mac
  
    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    ```
    
  - Ubuntu
  
    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    ```
  
  以下のコマンドでインストールできているか確認
  
  ```bash
  pyenv --version 
  # pyenv 2.64.3
  ```
  
- とりあえず，何かしらのバージョン(3.3以上)のPythonをインストールする

  ```bash
  pyenv install x.x.x
  pyenv global x.x.x
  pyenv rehash
  ```

### 移行作業

- Pythonの現在のバージョンの確認

  `*`が現在のPythonのバージョン

  ```bash
  pyenv versions
  > * 3.8.7 (set by C:\Users\Administrator\.pyenv\pyenv-win\version)
  ```

  - Pythonのバージョンをインストール（なければ）

    ```bash
    pyenv install x.x.x
    ```
  
- プロジェクトディレクトリにコマンドで移動

  ```bash
  cd /path/to/project
  ```

- Pythonのバージョンを指定

  `local`オプションでそのディレクトリ内でのみ使用するPythonのバージョンを指定できる

  ```bash
  pyenv local x.x.x
  pyenv versions
  > 
  ```

- 仮想環境の作成

  `.venv`は任意だが，`.venv`が一般的．

  ```bash
  python -m venv .venv
  ```

- 仮想環境をActivate

  ```bash
  # コマンドプロンプトの場合
  .venv/Scripts/activate.bat
  # Git bashの場合
  source .venv/Scripts/activate
  ```

- 必要なモジュールのインストール

  プロジェクトディレクトリに先ほどの`{}.txt`をコピペして，以下コマンド実行
  
  ```bash
  pip install -r {}.txt
  ```

  

## 参考サイト

[Anaconda パッケージリポジトリが「大規模な」商用利用では有償になっていた](https://qiita.com/tfukumori/items/f8fc2c53077b234384fc)

[Anacondaの有償化に伴いminiconda+conda-forgeでの運用を考えてみた](https://qiita.com/kimisyo/items/986802ea52974b92df27)

[Windows 10 で pyenv + pipenv の環境で Pythonを使いたい](https://qiita.com/akym03/items/3576842eed0e9d28cf82)