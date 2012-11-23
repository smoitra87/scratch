""" 
Learning objectives : 
Decorators
@task decorator
Roles
Executing functions in order so that they set up the environment variables
"""

from fabric.api import *

env.hosts=["pisa.lti.cs.cmu.edu","127.0.0.1"]
env.roledefs={"server":["pisa.lti.cs.cmu.edu"],"workstation":["127.0.0.1"]}
env.user="subhodeep"
#env.parallel=True
env.parallel=False
env.skip_bad_hosts=True
env.timeout=1
env.warn_only=True

@with_settings(warn_only=True)
@hosts("pisa.lti.cs.cmu.edu")
def install(package="python-networkx"):
    sudo("apt-get install %s" % package)

@roles("server")
def nose():
    sudo("apt-get install -y python-nose")

def test():
    env.hosts=["127.0.0.1"]
    env.user="subhodeep"
    env.warn_only=True
    env.parallel=True

def production():
    env.hosts=["subhodeep@pisa.lti.cs.cmu.edu"]
    env.skip_bad_hosts=True

