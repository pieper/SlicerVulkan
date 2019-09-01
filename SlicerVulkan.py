
"""

exec(open('c:\\pieper\\slicer4\\latest\\SlicerVulkan\\SlicerVulkan.py').read())


"""

slicer.mrmlScene.Clear(0)
slicer.util.delayDisplay("Starting",1)

import SampleData
mrHead = SampleData.downloadSample('MRHead')
slicer.util.delayDisplay("Head downloaded...",1)

import subprocess

import os; os.chdir('c:\\pieper\\slicer4\\latest\\SlicerVulkan\\vulkan\\example\\contribs')

compiler = 'c:/VulkanSDK/1.1.108.0/Bin/glslangValidator.exe'
subprocess.run([compiler, '-V', 'mandelbrot_compute.comp', '-o', 'mandelbrot_compute.spv'])

exec(open('example_mandelbrot_compute.py').read())

# slicer.util.loadVolume('mandelbrot.png')
