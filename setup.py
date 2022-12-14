import pathlib
import os
from subprocess import check_call

def generate_proto_code():
    proto_interface_dir = "./protos"
    generated_src_dir = "./service"
    service_proto_name = "inventoryService.proto"
    if not os.path.exists(generated_src_dir):
        os.mkdir(generated_src_dir)
    proto_it = pathlib.Path().glob(proto_interface_dir + "/**/*.proto")
    proto_path = proto_interface_dir
    protos = [str(proto) for proto in proto_it if proto.is_file()]
    check_call(["protoc"] + protos + ["--python_out", generated_src_dir, "--proto_path", proto_path])

    # generate server code
    #os.system('python3 -m grpc_tools.protoc --proto_path=./protos --python_out=./service --grpc_python_out=./service inventoryService.proto')

    cmd = 'python3 -m grpc_tools.protoc ' + \
        '--proto_path=' + \
        proto_interface_dir + ' ' + \
        '--python_out=' + \
        generated_src_dir + ' ' + \
        '--grpc_python_out=' + \
        generated_src_dir + ' ' + \
        service_proto_name

    os.system(cmd)


from setuptools.command.develop import develop
from setuptools import setup, find_packages

class CustomDevelopCommand(develop):
    """Wrapper for custom commands to run before package installation."""
    uninstall = False

    def run(self):
        develop.run(self)

    def install_for_development(self):
        develop.install_for_development(self)
        generate_proto_code()


setup(
    name='testpkg',
    version='1.0.0',
    package_dir={'': 'src'},
    cmdclass={
        'develop': CustomDevelopCommand, # used for pip install -e ./
    },
    packages=find_packages(where='src')
)