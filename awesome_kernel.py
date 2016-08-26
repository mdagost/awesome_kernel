from ipykernel.kernelbase import Kernel

class EverythingIsAwesomeKernel(Kernel):
    implementation = ''
    implementation_version = ''
    language = ''
    language_version = ''
    banner = language + language_version + '\n'
    language_info = {
        'name': 'everything_is_awesome',
        'codemirror_mode': 'python',
        'mimetype': 'text/x-sh',
        'file_extension': '.py'
    }

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        stream_content = {'data': {'text/html': '<iframe width="560" height="315" src="https://www.youtube.com/embed/StTqXEQ2l-Y" frameborder="0" allowfullscreen></iframe>'}}
        self.send_response(self.iopub_socket, 'display_data', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
            }
        
if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=EverythingIsAwesomeKernel)
