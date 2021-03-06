#!/usr/bin/env python

import json
import os
import requests
import shlex
import socket
import sys

# https://cwiki.apache.org/confluence/display/AMBARI/Blueprints#Blueprints-Step4:SetupStackRepositories%28Optional%29 
'''
PUT /api/v1/stacks/:stack/versions/:stackVersion/operating_systems/:osType/repositories/:repoId
 
{
  "Repositories" : {
    "base_url" : "<CUSTOM_REPO_BASE_URL>",
    "verify_base_url" : true
  }
}
'''

'''
[vagrant@sandbox ~]$ curl -u admin:admin http://$(hostname -f):8080/api/v1/stacks/OD/versions/0.9/operating_systems/redhat7
{
  "href" : "http://sandbox.odp.org:8080/api/v1/stacks/ODP/versions/0.9/operating_systems/redhat7",
  "OperatingSystems" : {
    "os_type" : "redhat7",
    "stack_name" : "ODP",
    "stack_version" : "0.9"
  },
  "repositories" : [
    {
      "href" : "http://sandbox.odp.org:8080/api/v1/stacks/ODP/versions/0.9/operating_systems/redhat7/repositories/ODP-0.9",
      "Repositories" : {
        "os_type" : "redhat7",
        "repo_id" : "ODP-0.9",
        "stack_name" : "ODP",
        "stack_version" : "0.9"
      }
    },
    {
      "href" : "http://sandbox.odp.org:8080/api/v1/stacks/ODP/versions/0.9/operating_systems/redhat7/repositories/ODP-UTILS-1.1.0.20",
      "Repositories" : {
        "os_type" : "redhat7",
        "repo_id" : "ODP-UTILS-1.1.0.20",
        "stack_name" : "ODP",
        "stack_version" : "0.9"
      }
    }
  ]
'''

def post_repo(stackname, stackversion, ostype, repoid, repourl):

    # ODP 0.9 redhat7 ODP-0.9 http://repo.opendataplatform.org/repository/ODP/centos7/2.x/BUILDS/0.9.0.1-70

    data = {
      "Repositories" : {
        "base_url" : "%s" % repourl,
        "verify_base_url" : True
      }
    }

    hostname = socket.gethostname()
    headers = {'X-Requested-By': 'FOOBAR'}
    baseurl = "http://%s:8080/api/v1" % (hostname)
    baseurl += "/stacks/%s/versions/%s/operating_systems/%s/repositories/%s"  % (stackname, stackversion, ostype, repoid)

    print "# PUT --> %s" % baseurl
    r = requests.put(baseurl, auth=('admin', 'admin'), data=json.dumps(data), headers=headers)

    print "# %s" % r.status_code
    for x in r.text.split('\n'):
        print "# %s" % x

if __name__ == "__main__":

    # ODP 0.9 redhat7 ODP-0.9 http://repo.opendataplatform.org/repository/ODP/centos7/2.x/BUILDS/0.9.0.1-70
    # ODP 0.9 redhat7 ODP-UTILS-1.1.0.20 http://repo.opendataplatform.org/repository/ODP-UTILS-1.1.0.20/repos/centos7
    print sys.argv
    assert len(sys.argv) >= 2, "Usage: <SCRIPT> <stackname> <stackversion> <ostype> <repoid> <repourl>"

    stackname = sys.argv[1]
    stackversion = sys.argv[2]
    ostype = sys.argv[3]
    repoid = sys.argv[4]
    repourl = sys.argv[5]

    post_repo(stackname, stackversion, ostype, repoid, repourl)
