# Manage VMs on VSphere

## prerequisites

1. Ensure Python is available on the local machine and create a new Virtual Environment called `etx` and activate the newly created Virtual Environment

```sh
python -m venv etx
source etx/bin/activate
```

2. Install required Python dependencies

```sh
pip install ansible-navigator
```

3. Ensure that Podman is install and login to Quay so that required container images can be retrieved

```sh
podman login quay.io/redhat-cop/virt-migration-factory-ee
```

Create a file called `setenv.sh` with the following contents:

```sh
export VSPHERE_PASSWORD="your password"
```

## Create VMs

Inspect the [vars.yml](vars.yml) to confirm the expected values are set. Be sure to verify the desired number of students in the `students_count` variable.

Execute the following:

```sh
source setenv.sh
ansible-navigator run --pp=missing --eei=quay.io/redhat-cop/virt-migration-factory-ee:latest --pp=missing -m stdout --penv VSPHERE_PASSWORD --pae=false content/ansible/create_vms.yml
```

## Clean up

Execute the following

```sh
source setenv.sh
ansible-navigator run --pp=missing --eei=quay.io/redhat-cop/virt-migration-factory-ee:latest --pp=missing -m stdout --penv VSPHERE_PASSWORD --pae=false content/ansible/remove_vms.yml
```