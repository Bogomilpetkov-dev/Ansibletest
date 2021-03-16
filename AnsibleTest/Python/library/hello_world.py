#!/usr/bin/python

from ansible.module_utils.basic import * ## import the ansible.module_utils.basic to use AnsibleModule

def main():
    module = AnsibleModule(argument_spec={})
    theReturnValue = {"hello": "world"}
    module.exit_json(changed=False, meta=theReturnValue)

if __name__ == '__main__':
    main()