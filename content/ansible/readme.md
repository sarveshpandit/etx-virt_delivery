# Manage VMs on VSphere

## prerequisites

1. Ensure Python is available on the local machine and create a new Virtual Environment called `etx` and activate the newly created Virtual Environment

```sh
python -m venv ~/etx
```

```sh
source ~/etx/bin/activate
```

2. Install required Python dependencies

Create a file called `content/ansible/setenv.sh` with the following contents:

```sh
export VSPHERE_PASSWORD="your password"
export quay_user="your quay username"
export quay_password="your quay password"
```

install ansible navigator

```sh
pip install ansible-navigator
```

3. Ensure that Podman is install and login to Quay so that required container images can be retrieved

```sh
chmod +x content/ansible/setenv.sh
```

```sh
source content/ansible/setenv.sh
```

```sh
podman login --username $quay_user --password $quay_password quay.io/redhat-cop/virt-migration-factory-ee
```

## Create VMs

Inspect the [vars.yml](vars.yml) to confirm the expected values are set. Be sure to verify the desired number of students in the `students_count` variable.

Execute the following:

```sh
chmod +x content/ansible/setenv.sh
```

```sh
source content/ansible/setenv.sh
```

```sh
ansible-navigator run --eei=quay.io/redhat-cop/virt-migration-factory-ee:latest --pp=missing -m stdout --penv VSPHERE_PASSWORD --pae=false content/ansible/create_vms.yml
```

## Clean up

Execute the following

```sh
chmod +x content/ansible/setenv.sh
```

```sh
source content/ansible/setenv.sh
```

```sh
ansible-navigator run --eei=quay.io/redhat-cop/virt-migration-factory-ee:latest --pp=missing -m stdout --penv VSPHERE_PASSWORD --pae=false content/ansible/remove_vms.yml
```
