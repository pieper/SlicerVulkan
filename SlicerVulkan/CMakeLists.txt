cmake_minimum_required(VERSION 3.13.4)

project(SlicerVulkan)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/SlicerVulkan")
set(EXTENSION_CATEGORY "GPU")
set(EXTENSION_CONTRIBUTORS "Steve Pieper (Isomics, Inc.)")
set(EXTENSION_DESCRIPTION "Access GPU computing via the python Vulkan API.")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/SlicerVulkan.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/SlicerVulkan/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(VulkanFilters)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
