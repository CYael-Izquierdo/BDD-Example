import xmlrpc.client
import base64
from features.steps.constants import Constants


class TestlinkAPIClient:
    # substitute your server URL Here

    def __init__(self):
        self.server = xmlrpc.client.ServerProxy(Constants.TL_URL)
        self.devKey = Constants.TL_DEV_KEY

    def uploadExecutionAttachment(self, executionid, filename, filetype, content, title, description):
        data = {"executionid": executionid,
                "devKey": self.devKey,
                "filename": filename,
                "filetype": filetype,
                "content": content,
                "title": title,
                "description": description}
        return self.server.tl.uploadExecutionAttachment(data)

    def reportTCResult(self, testcaseid, testplanid, status, buildname, platformname, execduration, steps):
        data = {"devKey": self.devKey,
                "testcaseid": testcaseid,
                "testplanid": testplanid,
                "status": status,
                "buildname": buildname,
                "platformname": platformname,
                "execduration": execduration,
                "steps": steps}
        return self.server.tl.reportTCResult(data)

    def getProjects(self):
        data = {"devKey": self.devKey}
        return self.server.tl.getProjects(data)

    def getProjectTestPlans(self, project_id):
        data = {"devKey": self.devKey, "testprojectid": project_id}
        return self.server.tl.getProjectTestPlans(data)

    def getTestCaseIDByName(self, tc_name, ts_name='', tp_name='', tc_path=''):
        data = {"devKey": self.devKey, "testcasename": tc_name}
        if ts_name:
            data["testsuitename"] = ts_name
        if tp_name:
            data["testprojectname"] = tp_name
        if tc_path:
            data["testcasepathname"] = tc_path
        return self.server.tl.getTestCaseIDByName(data)

    def getInfo(self):
        return self.server.tl.about()
