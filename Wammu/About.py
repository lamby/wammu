# -*- coding: ISO-8859-2 -*-

import wx
import wx.html
import wx.lib.wxpTag
import sys
import gammu
import Wammu

if wx.USE_UNICODE:
    header = ''
    copyright = 'Copyright &copy; 2003-2004 Michal &#268;iha&#345;'
else:
    header = '<head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-2"></head>'
    copyright = 'Copyright (c) 2003-2004 Michal �iha�'

text = '''
<html>
%s
<body>
<center><table bgcolor="#458154" width="100%%" cellspacing="0"
cellpadding="0" border="1">
<tr>
    <td align="center">
    %s
    </td>
</tr>
</table>

<p>%s</p>

<p>
<font size=-3>
%s
<br><br>
%s
<br><br>
%s
</font>
</p>
<p>
<wxp module="wx" class="Button">
    <param name="label" value="%s">
    <param name="id"    value="ID_OK">
</wxp>
</p>
</center>
</body>
</html>

''' % (header,
    '''
    <h2>Wammu %s</h2>
    %s<br>
    %s<br>
    %s<br>
''' % (Wammu.__version__,
    _('Running on Python %s') % sys.version.split()[0],
    _('Using wxPython %s') % wx.VERSION_STRING,
    _('Using python-gammu %s and Gammu %s') %  (gammu.Version()[1], gammu.Version()[0])),
    _('<b>Wammu</b> is a wxPython based GUI for Gammu.'),
    copyright,
    _('''
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
'''),
    _('''
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''),
    _('OK'))

class AboutBox(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, _('About Wammu'))
        html = wx.html.HtmlWindow(self, -1, size = (500, -1))
        html.SetPage(text)
        btn = html.FindWindowById(wx.ID_OK)
        if btn != None:
            btn.SetDefault()
        ir = html.GetInternalRepresentation()
        html.SetSize( (ir.GetWidth()+25, ir.GetHeight()+25) )
        self.SetClientSize(html.GetSize())
        self.CentreOnParent(wx.BOTH)
