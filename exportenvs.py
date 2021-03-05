import subprocess, sys, os
outputs = subprocess.check_output('conda env list').splitlines()
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
envs.remove('base')
print('export yml and txt for all environments')
for i, e in enumerate(envs):
    sys.stdout.write('\r Exporting {}: {}/{}'.format(e, i+1, len(envs)))
    sys.stdout.flush()
    #_ = os.system('conda env export -n {0} > {0}.yml'.format(e))
    _ = os.system('conda activate {0} && pip freeze > {0}.txt'.format(e))

