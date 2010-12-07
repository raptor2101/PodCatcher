# -*- coding: utf-8 -*-
#-------------LicenseHeader--------------
# plugin.audio.podcatcher - A plugin to play Podcasts
# Copyright (C) 2010  Raptor 2101 [raptor2101@gmx.de]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
import xbmcaddon, os, pickle;
from xml.dom import minidom


class ArchiveFile(object):
  def __init__(self, itemId):
    global __archiveDir__;
    
    self.feedItems = [];
    self.lastLoad = 0;
    
    self.archiveFile = os.path.join(__archiveDir__,itemId);
    
    if os.path.exists(self.archiveFile):
      input = open(self.archiveFile, 'r')
      unsortedObject = pickle.load(input);
      self.feedItems = sorted(unsortedObject, key = lambda item:item.date, reverse=True);
      self.lastLoad = stats = os.stat(self.archiveFile)[8];
  
  @classmethod
  def setArchivePath(self, path):
    global __archiveDir__;
    __archiveDir__ = path;
  
  def save(self):
    output = open(self.archiveFile, 'w')
    pickle.dump(self.feedItems, output);