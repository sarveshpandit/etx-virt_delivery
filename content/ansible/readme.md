# Manage VMs on VSphere

## prerequisites

create a file called setenv.sh with teh following content:

```sh
export vsphere_password="your password"
ansible-galaxy collection install community.vmware
```

## create VM

inspect the vars.yaml, mainly make sure that you have the right number of students.
run the following:

```sh
./setenv.sh
ansible-playbook create_vms.yaml
```

## Clean up

run the following

```sh
./setenv.sh
ansible-playbook remove_vms.yaml
```