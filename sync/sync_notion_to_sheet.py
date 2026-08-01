Run python sync/sync_notion_to_sheet.py
Traceback (most recent call last):
  File "/home/runner/work/hoaxempire-mxtw/hoaxempire-mxtw/sync/sync_notion_to_sheet.py", line 107, in <module>
    main()
  File "/home/runner/work/hoaxempire-mxtw/hoaxempire-mxtw/sync/sync_notion_to_sheet.py", line 101, in main
    ws.append_row(row)
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/gspread/worksheet.py", line 1812, in append_row
    return self.append_rows(
           ^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/gspread/worksheet.py", line 1862, in append_rows
    res = self.client.values_append(self.spreadsheet_id, range_label, params, body)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/gspread/http_client.py", line 191, in values_append
    r = self.request("post", url, params=params, json=body)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/gspread/http_client.py", line 128, in request
    raise APIError(response)
gspread.exceptions.APIError: APIError: [429]: Quota exceeded for quota metric 'Write requests' and limit 'Write requests per minute per user' of service 'sheets.googleapis.com' for consumer 'project_number:116321911525'.
Error: Process completed with exit code 1.
