# Synopsis

This is a QGIS plugin written in Python.

It attempts to find the highest possible number of points in polygons if a certain distance between the points is given. Outputs a multipoint layer.

# Usage

This algorithm takes a polygon layer and asks you to enter a "Distance between points" value. Taking the distance constraint into account, it attempts to find an arrangement of points within each polygon that yields the highest possible number of points (note the caveat in the following paragraph). The algorithm outputs a multipoint layer containing one feature for each feature from the input layer. Its attributes are an "FID" (int) field referring to the input feature's fid and a "NUMPOINTS" (int) field stating the number of points that were fitted. The multipoint geometry contains an arrangement of points that yielded the highest number of points.

Please bear in mind that this is an approximation algorithm that is based on testing a large number of possible point arrangements. This approach does not make it possible to find the very best solution with certainty.\n\nThe basis for the testing process are regular point grids. You can choose whether you would like the algorithm to use square based grids, triangle based grids or both. Please note that square based grids provide the optimum result only in special cases (relatively small, rectangular input polygons).

The algorithm takes the grids and varies them by moving them step by step in the x-direction and y-direction and rotating them (and all of them at the same time). You can specify how many iterations you want to be performed for each of these factors. Here is an example to help you understand this: If you have specified 500 metres as the distance and 10 as the number of iterations (x-direction), the grid is moved horizontally in steps of 50 metres. The range for rotation iterations is between 0 and 90 degrees for square based grids and 0 to 120 degrees for triangle based grids. Further rotations would not usually lead to better results.

Higher numbers of iterations do not necessarily lead to better results (it is even possible to get worse results). As a starting point, use the default values and then experiment with different settings.

# License

**Put spaced points in polygons (pspip)** -- a QGIS plugin attempting to find the highest possible number of points in polygons if a certain distance between the points is given.
Copyright (C) 2024 Ch. Lesem

This program is free software; you can redistribute it and/or modify
it under the terms of the **GNU General Public License** as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# How to install

- download this zip archive: https://github.com/Sempione/pspip/archive/refs/heads/main.zip
- unzip the archive and move the resulting directory into the QGIS plugins directory
 (on Windows usually "C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins" replace "USER" by the actual user name)
- search for "Put spaced points in polygons" in the QGIS plugin manager and install it
- the plugin is now in the QGIS processing toolbox (section: "pspip")
