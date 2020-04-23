#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time      : 2020/4/23
# @Author    : Roger
# @File      : html.py
# @Software  : PyCharm
# @Desc      :

import datetime


def to_html(filename,title, result):
    today = datetime.datetime.now().strftime('%Y%m%d')
    html_tpl = '''
        <!DOCTYPE html>
            <html>
           <head>
           <meta charset="utf-8"/>
           <title>{title}</title>
           <style type="text/css">	
               body {{
                   margin:0;
                   padding:0;
                   font:14px/15px "Helvetica Neue",Arial, Helvetica, sans-serif;
                   color: #555;
               }}
               a {{color:#666;}}
               #content {{width:70%; max-width:1920px; margin:0 auto;}}
               table {{
                   overflow:hidden;
                   border:1px solid #d3d3d3;
                   background:#fefefe;
                   width:100%;
                    margin:0 auto;
                   -moz-border-radius:5px; /* FF1+ */
                   -webkit-border-radius:5px; /* Saf3-4 */
                   border-radius:5px;
                   -moz-box-shadow: 0 0 4px rgba(0, 0, 0, 0.2);
                   -webkit-box-shadow: 0 0 4px rgba(0, 0, 0, 0.2);
               }}
               table caption {{font-size: 30px; font-weight:bold;margin:30px auto;}}
               th, td {{padding:18px 28px 18px; text-align:center; }}
               th {{padding-top:22px; text-shadow: 1px 1px 1px #fff; background:#e8eaeb;}}
               td {{border-top:1px solid #e0e0e0; border-right:1px solid #e0e0e0;}}
               tr.odd-row td {{background:#f6f6f6;}}
               td.first, th.first {{text-align:left}}
               td.last {{border-right:none;}}
               td {{
                   background: -moz-linear-gradient(100% 25% 90deg, #fefefe, #f9f9f9);
                   background: -webkit-gradient(linear, 0% 0%, 0% 25%, from(#f9f9f9), to(#fefefe));
               }}
               tr.odd-row td {{
                   background: -moz-linear-gradient(100% 25% 90deg, #f6f6f6, #f1f1f1);
                   background: -webkit-gradient(linear, 0% 0%, 0% 25%, from(#f1f1f1), to(#f6f6f6));
               }}
               th {{
                   background: -moz-linear-gradient(100% 20% 90deg, #e8eaeb, #ededed);
                   background: -webkit-gradient(linear, 0% 0%, 0% 20%, from(#ededed), to(#e8eaeb));
               }}
               tr:first-child th.first {{
                   -moz-border-radius-topleft:5px;
                   -webkit-border-top-left-radius:5px; /* Saf3-4 */
               }}
               tr:first-child th.last {{
                   -moz-border-radius-topright:5px;
                   -webkit-border-top-right-radius:5px; /* Saf3-4 */
               }}
               tr:last-child td.first {{
                   -moz-border-radius-bottomleft:5px;
                   -webkit-border-bottom-left-radius:5px; /* Saf3-4 */
               }}
               tr:last-child td.last {{
                   -moz-border-radius-bottomright:5px;
                   -webkit-border-bottom-right-radius:5px; /* Saf3-4 */
               }}
           </style>
           </head>
           <body>
           <div id="content">
               <table cellpadding="0" cellspacing="0">
               <!-- <caption>{title}</caption> -->
                   <thead>
                        <tr>
                            {thead}
                        </tr>
                    </thead>
                    <tbody>
                        {tbody}
                    </tbody>
                </table>
            </div>
            <script type="text/javascript">
                    var index = 0;
                    var tableElements = document.getElementsByTagName("tr");
                    for (index = 0;index<tableElements.length;index++) {{
                        if (index % 2) == 0{{
                            tableElements[index].className="odd-row"
                            }}
                        }}
            </script>
           </body>
           </html>
           '''
    file = './{filename}_{today}.html'.format(filename=filename, today=today)
    htmlhandle = open(file, 'w+')
    title = '{title}'.format(title=title)
    thead = '<th>IP</th><th>database</th><th>result</th>'
    tbody = ''
    for row in result:
        ip = row[0]
        dsn = row[1]
        values = row[2]
        if values:
            tbody += '<tr>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n</tr>\n' % (ip, dsn, values)
    ss=html_tpl.format(title=title, thead=thead, tbody=tbody)
    htmlhandle.write(ss)
    htmlhandle.close()
