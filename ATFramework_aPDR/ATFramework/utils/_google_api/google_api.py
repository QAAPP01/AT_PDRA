# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# install library
# $ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
TOKEN_FILE = 'token.pickle'
CREDENTIALS_FILE = 'credentials.json'

class GoogleApi():

    # header_list: a list of report header. e.g. ['Date', 'Time', 'Server', 'OS', 'Device', 'Version', 'Pass', 'Fail', 'Skip', 'N/A', 'Total time']
    def __init__(self, sheet_name='sample', header_custom=[], row_start=1, spreadsheet_id='1tjQIUCl5HfEPKCGCEHuRS0_HP-72eYB8tsZKUvE6_v4'):
        try:
            print('Google_Api __init__ start')
            header_template = ['Date', 'Time', 'Script_Name', 'Script_Ver', 'SR_No', 'TR_No', 'Build_No', 'Prod_Ver', 'Prod_Ver_Type', 'OS', 'OS_Ver', 'Device_ID']
            header_list = header_template + header_custom
            # init. row dict (for batch update values)
            row_dict = {}
            for key in header_list:
                row_dict[key] = ''
            creds = None
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            file_path_token = os.path.join(os.path.dirname(__file__), TOKEN_FILE)
            file_path_credentials = os.path.join(os.path.dirname(__file__), CREDENTIALS_FILE)
            if os.path.exists(file_path_token):
                with open(file_path_token, 'rb') as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        file_path_credentials, SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(file_path_token, 'wb') as token:
                    pickle.dump(creds, token)

            self.service = build('sheets', 'v4', credentials=creds)
            self.row_start=row_start
            self.spreadsheet_id = spreadsheet_id
            self.sheet_name = sheet_name
            self.create_new_sheet(sheet_name)
            self.row_prev_record = row_start
            self.header = {}
            self.set_header(header_list, row_start)
            self.row_dict = row_dict # for batch update
            print('service is built.')
        except Exception as e:
            print(e)
            raise Exception

    def set_header(self, header_list, row=1):
        try:
            header_dict = {}
            column_num = 1
            for value in header_list:
                header_dict[chr(ord('@')+column_num)] = value
                column_num += 1
            self.header = header_dict
            print(self.header)
            # check if header already exists
            response = self.get_columns(row)
            if 'values' in list(response['valueRanges'][0].keys()):
                return True
            print('No header is found. Create it.')
            sheet = self.service.spreadsheets()
            last_key_of_header = list(self.header.keys())[-1]
            print(f'last key of dict:{last_key_of_header}')
            # set batch structure
            body = {
                "valueInputOption": 'USER_ENTERED',
                "data": [{
                    "range": self.sheet_name + f'!A{row}:{last_key_of_header}',
                    "majorDimension": "ROWS",
                    "values": [header_list]
                }]
            }
            sheet.values().batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
            # # batch update cell format
            # # > get sheet id by name
            # spreadsheet = self.service.spreadsheets().get(spreadsheetId=self.spreadsheet_id).execute()
            # sheet_id = None
            # for _sheet in spreadsheet['sheets']:
            #     if _sheet['properties']['title'] == self.sheet_name:
            #         sheet_id = _sheet['properties']['sheetId']
            #
            # print(f"{self.sheet_name}={sheet_id}")
            # batch_update_spreadsheet_request_body = {
            #     'requests': {
            #         "repeatCell": {
            #             "cell": {
            #                 "userEnteredFormat": {
            #                     "backgroundColor": {
            #                         "red": 0,
            #                         "green": 0,
            #                         "blue": 0,
            #                         "alpha": 1
            #                     },
            #                     "horizontalAlignment": "CENTER",
            #                     "verticalAlignment": "MIDDLE",
            #                     "textFormat": {
            #                         "foregroundColor": {
            #                             "red": 1,
            #                             "green": 1,
            #                             "blue": 1,
            #                             "alpha": 1
            #                         },
            #                         "fontSize": 12,
            #                         "bold": True,
            #                     },
            #                 }
            #             },
            #             "range": {
            #                 "sheetId": sheet_id,
            #                 "startRowIndex": row - 1,
            #                 "endRowIndex": row,
            #                 "startColumnIndex": 0,
            #                 "endColumnIndex": len(self.header.keys()),
            #             },
            #             "fields": "userEnteredFormat"
            #         }
            #     }
            # }
            # self.service.spreadsheets().batchUpdate(
            #     spreadsheetId=self.spreadsheet_id, body=batch_update_spreadsheet_request_body).execute()
        except Exception as e:
            print(e)
            raise Exception
        return True

    def create_new_sheet(self, sheet_name):
        try:
            sheets_list = self.get_sheets_title_list()
            if sheet_name not in sheets_list:
                sheet = self.service.spreadsheets()
                request_body = {
                    'requests': [{
                        'addSheet': {
                            'properties': {
                                'title': sheet_name,
                            }
                        }
                    }]
                }

                response = sheet.batchUpdate(
                    spreadsheetId=self.spreadsheet_id,
                    body=request_body
                ).execute()

                return response
            else:
                print(f'{sheet_name=} already exists.')
                return True
        except Exception as e:
            print(e)

    def get_sheets_title_list(self):
        try:
            sheet = self.service.spreadsheets()
            sheet_metadata = sheet.get(spreadsheetId=self.spreadsheet_id).execute()
            sheets = sheet_metadata.get('sheets', '')
            title_list = []
            for index in range(len(sheets)):
                title = sheets[index].get("properties", {}).get("title", "Sheet1")
                title_list.append(title)
            return title_list
        except Exception as e:
            print(e)

    def add_new_record(self, data): # data: dictionary e.g. {'Date': '2020/08/14_11:34'}
        try:
            sheet = self.service.spreadsheets()
            for key in data.keys():
                if key in self.row_dict.keys():
                    self.row_dict[key] = data[key]
            print(self.row_dict)
            data_list = list(self.row_dict.values())
            print(data_list)
            last_key_of_header = list(self.header.keys())[-1]
            print(f'last key of dict:{last_key_of_header}')
            #get the last row
            result = sheet.values().get(spreadsheetId=self.spreadsheet_id,
                                        range=self.sheet_name).execute()
            values = result.get('values', [])
            target_row = self.row_start + len(values)
            self.row_prev_record = target_row
            print(f'{target_row=}')
            # set batch structure
            body = {
                "valueInputOption": 'USER_ENTERED',
                "data": [{
                    "range": self.sheet_name + f'!A{target_row}:{last_key_of_header}',
                    "majorDimension": "ROWS",
                    "values": [data_list]
                }]
            }
            sheet.values().batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
        except Exception as e:
            print(e)
            raise Exception
        return target_row

    def update_column(self, column_name, data, target_row=-1): # data: string
        try:
            sheet = self.service.spreadsheets()
            record_list = [[data],]
            content_body = {
                "values": record_list
            }
            if target_row == -1:
                target_row = self.row_prev_record
            range_name = self.sheet_name + f'!{column_name}{target_row}'
            result = sheet.values().update(
                spreadsheetId=self.spreadsheet_id, range=range_name,
                valueInputOption='USER_ENTERED', body=content_body).execute() # 2020/12/23 modify valueInputOption from 'RAW' to 'USER_ENTERED' as Bill's request
        except Exception as e:
            print(e)
            raise Exception
        return True

    def update_columns(self, data, target_row=-1): # data - dictionary e.g. data = {'B':'FAIL', 'C':'1:33:22'}
        try:
            sheet = self.service.spreadsheets()
            if target_row == -1:
                target_row = self.row_prev_record
            print(f'{target_row=}')
            for key in data.keys():
                if key in self.row_dict.keys():
                    self.row_dict[key] = data[key]
            print(self.row_dict)
            data_list = list(self.row_dict.values())
            print(data_list)
            last_key_of_header = list(self.header.keys())[-1]
            print(f'last key of dict:{last_key_of_header}')
            body = {
                    "valueInputOption": 'USER_ENTERED',
                    "data": [{
                        "range": self.sheet_name + f'!A{target_row}:{last_key_of_header}',
                        "majorDimension": "ROWS",
                        "values": [data_list]
                    }]
            }
            sheet.values().batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
        except Exception as e:
            print(e)
            raise Exception
        return True

    def get_columns(self, target_row=-1):
        try:
            last_key_of_header = list(self.header.keys())[-1]
            if target_row == -1:
                target_row = self.row_prev_record
            ranges = self.sheet_name + f'!A{target_row}:{last_key_of_header}'
            response = self.service.spreadsheets().values().batchGet(spreadsheetId=self.spreadsheet_id, ranges=ranges, majorDimension='ROWS').execute()
        except Exception as e:
            print(e)
            raise Exception
        return response

    def update_result(self, data, target_row=-1):
        try:
            self.update_columns(data, target_row)
        except Exception:
            raise Exception
        return True


if __name__ == '__main__':
    # Test Code ==========================
    # initial google_api object
    spreadsheet_id = '1iQsmn5QOddwovzaxb5fcQt3gR2Ts__6iajQm4CSd4Oo' # google_sheet_api_test
    sheet_name = 'test_sheet'
    header_custom = ['Pass', 'Fail', 'Skip', 'N/A', 'Total time']
    obj_google_api = GoogleApi(sheet_name, header_custom, 1, spreadsheet_id)

    # add new record w/ test information
    import datetime
    now = datetime.datetime.now()
    new_record = {'Date': now.date().strftime("%Y-%m-%d"),
                  'Time': now.time().strftime("%H:%M:%S"),
                  'Script_Name': 'aU_SFT',
                  'Script_Ver': '1.0.0',
                  'SR_No': 'YOU200722-05',
                  'TR_No': '',
                  'Build_No': '209176',
                  'Prod_Ver': '6.2.0',
                  'Prod_Ver_Type': 'Prod',
                  'OS': 'Android',
                  'OS_Ver': '10.0',
                  'Device_ID': '98TAY16WK9'}
    obj_google_api.add_new_record(new_record)

    # update result of previous record
    data = {'Pass': '102', 'Fail': '0', 'Skip': '1', 'N/A': '0', 'Total time': '3:31:55'}
    obj_google_api.update_result(data)

    print(f'Done.')
