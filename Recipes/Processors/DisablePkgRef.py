#!/usr/local/autopkg/python

"""See docstring for DisablePkgRef class"""

import xml.etree.ElementTree as ET

from autopkglib import Processor

__all__ = ["DisablePkgRef"]


class DisablePkgRef(Processor):
    """Sets the 'active' attribute for a pkg-ref tag to false within a flatpackage's distribution file."""

    description = __doc__
    input_variables = {
        "input_distribution_path": {
            "required": True,
            "description": "File path to the distribution xml file to modify.",
        },
        "output_distribution_path": {
            "required": True,
            "description": "File path of the modified distribution xml file. Can be the same path as input_distribution_path.",
        },
        "bundle_id": {
            "required": True,
            "description": "The bundle identifier for the pkg-ref to disable.",
        },
    }
    output_variables = {}

    __doc__ = description

    def main(self):
        # read input string as an element tree
        inputXml = ET.parse(self.env['input_distribution_path'])
        root = inputXml.getroot()

        self.output(f"Grabbed file from {self.env['input_distribution_path']}")

        # find the relevant pkg-ref tag
        xPathStr = f"./pkg-ref[@id='{self.env['bundle_id']}'][@version]"
        self.output(f"Searching for the following element {xPathStr}")
        pkgRef = root.find(xPathStr)
        pkgRef.set("active", "false")

        # save the result
        outFile = open(self.env['output_distribution_path'], "wb")
        outFile.write(b'<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n')

        inputXml.write(outFile, encoding='UTF-8', xml_declaration=False)

        outFile.close()

if __name__ == "__main__":
    PROCESSOR = DisablePkgRef()
    PROCESSOR.execute_shell()