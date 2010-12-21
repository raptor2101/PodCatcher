# -*- coding: utf-8 -*-

def transformHtmlCodes(string):
  replacements = (
    (u'Ä', u'&Auml;'),
    (u'Ü', u'&Uuml;'),
    (u'Ö', u'&Ouml;'),
    (u'ä', u'&auml;'),
    (u'ü', u'&uuml;'),
    (u'ö', u'&ouml;'),
    (u'ß', u'&szlig;'),
    (u'\"',u'&#034;'),
    (u'\"',u'&quot;'),
    (u'\'',u'&#039;'),
    (u'&', u'&amp;')
  )
  for replacement in replacements:
    string = string.replace(replacement[1],replacement[0]);
  return string;
