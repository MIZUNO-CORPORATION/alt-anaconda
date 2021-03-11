import glob, os, sys

envs = glob.glob(os.path.join('.', '*.yml'))

for i, env in enumerate(envs):
    filename = os.path.basename(env)
    sys.stdout.write('\r Exporting {}: {}/{}'.format(env, i + 1, len(envs)))
    sys.stdout.flush()
    _ = os.system('conda env create -f {}'.format(filename))