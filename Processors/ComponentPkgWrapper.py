#!/usr/local/autopkg/python

import subprocess
import os

from autopkglib import Processor

__all__ = ["ComponentPkgWrapper"]

class ComponentPkgWrapper(Processor):
    description = ( "Wraps an existing component pkg into a distribution pkg using ProductBuild." )
    input_variables = {
        "pkg_path": {
            "required": True,
            "description": "Path to the component package."
        },
        "signing_cert": {
            "required": False,
            "description": "Optional name of the certificate used to sign the package. Must be an EXACT match. "
        },
        "output_pkg_name": {
            "required": True,
            "description": "The name of the output distribution package."
        }
    }
    output_variables = {
        "pkg_path": {
             "description": "Path to the output distribution package."
        }
    }

    __doc__ = description

    def main(self):
        pkg_dir = os.path.dirname( self.env[ "pkg_path" ] )

        command_line_list = [ "/usr/bin/productbuild" ]

        if self.env["signing_cert"]:
            command_line_list.extend(["--sign", self.env["signing_cert"]])
        
        command_line_list.extend(["--package", self.env["pkg_path"]])
        command_line_list.append(self.env["output_pkg_name"])

        print(command_line_list)

        subprocess.call(command_line_list)

        self.env["pkg_path"] = os.path.join(pkg_dir, self.env['output_pkg_name'])

if __name__ == '__main__':
    processor = ComponentPkgWrapper()
    processor.execute_shell()
