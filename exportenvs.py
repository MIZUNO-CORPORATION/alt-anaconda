import subprocess, sys, os
outputs = subprocess.check_output('conda env list', shell=True).splitlines()
startind = outputs.index(b'#')

# get all envs
envs = []
for o in outputs[startind+1:]:
    # convert byte to str
    line = o.decode('utf-8')
    if line == '':
        break
    envs += [line.split()[0]]

# remove base
#envs.remove('base')
print('export yml and txt for all environments')
for i, e in enumerate(envs):
    sys.stdout.write('\r Exporting {}: {}/{}'.format(e, i+1, len(envs)))
    sys.stdout.flush()
    _ = os.system('conda env export -n {0} > {0}.yml'.format(e))
    if os.name == 'nt':# windows
        with open(e + '.yml', 'r') as f:
            lines = f.readlines()
        if not lines[-1].startswith('prefix'):# remove [0m [0m
            with open(e + '.yml', 'w', encoding='utf-8') as f:
                f.writelines(lines[:-1])

        _ = os.system('conda activate {0} && pip list --format=freeze > {0}.txt'.format(e))
    else:
        _ = os.system('activate {0} && pip list --format=freeze > {0}.txt'.format(e))


