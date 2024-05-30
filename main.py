import subprocess
from utils import StreamLogger

stream_logger = StreamLogger()

def run_command(command):
    """Run a shell command and return the output and error."""
    stream_logger.stream_logger.system(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if output: stream_logger.stream_logger.info(output.decode('utf-8'))
    if error: stream_logger.stream_logger.error(error.decode('utf-8'))

def basics():
    run_command("minikube start")
    run_command("kind create cluster --image kindest/node:v1.23.5")
    run_command("kubectl config get-contexts")
    run_command("kubectl config current-context")
    run_command("kubectl config use-context minikube")
    run_command("kubectl config current-context")
    run_command("kubectl get nodes")
    run_command("kubectl get pods")

def get_command():
    run_command("kubectl get pods")
    run_command("kubectl get deployments")
    run_command("kubectl get services")
    run_command("kubectl get nodes")
    run_command("kubectl get secrets")
    run_command("kubectl get configmaps")
    run_command("kubectl get persistentvolumes")
    run_command("kubectl get ingress")
    run_command("kubectl get namespaces")


def namespaces():
    run_command("kubectl get namespaces")
    run_command("kubectl create namespace test")
    run_command("kubectl get namespaces")
    run_command("kubectl delete namespace test")
    run_command("kubectl get namespaces")


def describe():
    run_command("kubectl describe pods -n kube-system")

def version():
    run_command("kubectl version")

def deployment():
    # A Deployment controller provides declarative updates for Pods and ReplicaSets.
    # A Deployment is a set of Pods with the same configuration.

    run_command('kubectl apply -f deployment.yaml')
    run_command('kubectl get deploy')
    run_command('kubectl get po')
    run_command('kubectl describe deployments example-deploy')
    run_command('kubectl logs example-deploy-6c598cf449-fhm2r')
    pass


def config_map():
    # A config map is an API object used to store non-confidential data in key-value pairs.
    # A ConfigMap allows you to decouple environment-specific configuration from your container images,
    # so that your applications are easily portable.

    # Docker example
    # run_command(f'docker run -it -v ${PWD}/golang/configs/:/configs -v ${PWD}/golang/secrets/:/secrets aimvector/golang:1.0.0')
    
    # Kubernetes
    run_command('kubectl apply -f configmap.yaml')
    run_command('kubectl get cm')
    run_command('kubectl get configmaps')
    run_command('kubectl get configmaps example-config -o yaml')
    pass

def secrets():
    # A secret is an API object used to store sensitive data, such as passwords, API keys, and certificates.
    # Secrets can be used to store sensitive data in a Kubernetes cluster,
    # so that it can be accessed by applications running in different environments.

    # Docker example
    # run_command(f'docker run -it -v ${PWD}/golang/configs/:/configs -v ${PWD}/golang/secrets/:/secrets aimvector/golang:1.0.0')

    # Kubernetes
    run_command('kubectl apply -f secret.yaml')
    run_command('kubectl get secret')
    run_command('kubectl get secrets')
    run_command('kubectl get secrets mysecret -o yaml')
    pass



def load_balance_service_discovery():
    run_command('kubectl get deploy')
    run_command('kubectl get pods --show-labels')
    run_command('kubectl get svc')
    run_command('kubectl apply -f docker-development-youtube-series/kubernetes/services/service.yaml')
    run_command('kubectl get svc')
    run_command('kubectl describe svc example-service')
    pass



def main():
    # basics()
    # get_command()
    # namespaces()
    # describe()
    # version()
    # deployment()
    # config_map()
    load_balance_service_discovery()
    pass

if __name__ == "__main__":
    main()
    stream_logger.stream_logger.warning("Execution Stopped")
