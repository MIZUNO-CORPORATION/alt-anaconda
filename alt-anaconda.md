# Anaconda商用利用有償化対策

Anacondaの商用利用が有償化された（2020/04/10現在）．以下[Anaconda パッケージリポジトリが「大規模な」商用利用では有償になっていた](https://qiita.com/tfukumori/items/f8fc2c53077b234384fc)より．

> | 区分 | 条件                                                         |
> | ---- | ------------------------------------------------------------ |
> | 無償 | ・個人が個人的な非ビジネス目的で使用する<br/>・教育機関の学生または職員が教育活動に関連して使用する<br/>・慈善サービスの提供に関連して、非営利団体の従業員やボランティアが使用する、または<br/> ・従業員の総数が200人未満の共通支配下にある事業体（企業？）（[規約](https://www.anaconda.com/terms-of-service)では[entities](http://www.takahashi-office.jp/column/houritsu-keiyakusho/18.htm)と記載）が使用する |
> | 有償 | "無償"に記載した以外の条件でリポジトリを使用する場合         |

対策として，以下の２通りが候補として挙げられる．

|               |              メリット              | デメリット |
| :-----------: | -------------------------------- | -------- |
| [Miniconda+Pip](#Miniconda+Pip移行方法) | ・Anacondaと似たような使い方ができる | ・母体が同じなので，Anaconda同様商用利用有償化もありうる<br />・Anacondaほど扱っているパッケージが少ないので，結局Pipを使わないといけない<br/>＝パッケージ間のバージョンの競合の可能性は残る |
|  [Pyenv＋Pip](#Pyenv＋Pip移行方法)  | ・MITライセンスなので，有償化の心配は上記より少なそう | ・移行作業が少し大変<br />・パッケージ間のバージョンの競合しやすくなる |

## 移行する前に

まず，移行する前に仮想環境上のパッケージ情報を出力させる．

- 面倒な方→プログラムを作りました．（動作保証はしません）

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
  pip freeze > requrements.txt
  ```

## Miniconda＋Pip移行方法

- Windows
  
- Unix(Linux or Mac)


## Pyenv＋Pip移行方法