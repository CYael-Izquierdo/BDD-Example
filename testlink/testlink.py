import xmlrpc.client
import base64
from features.steps.constants import Constants


class TestlinkAPIClient:
    # substitute your server URL Here

    def __init__(self):
        self.server = xmlrpc.client.ServerProxy(Constants.TL_URL)
        self.devKey = Constants.TL_DEV_KEY

    def addTestCaseToTestPlan(self, testplanid, testcaseexternalid, testprojectid, version=1,
                              platformid=False, execution=2, status=2):
        data = {"devKey": self.devKey,
                "testprojectid": testprojectid,
                "testplanid": testplanid,
                "testcaseid": testcaseexternalid,
                "version": version,
                "execution": execution,
                "status": status}
        if platformid:
            data["platformid"] = platformid
        return self.server.tl.addTestCaseToTestPlan(data)

    def updateTestCase(self, testcaseid, version='', testcasename='', steps='', executiontype='', status=''):
        data = {"devKey": self.devKey,
                "testcaseid": testcaseid}
        if version:
            data['version'] = version
        if testcasename:
            data['testcasename'] = testcasename
        if steps:
            data['steps'] = steps
        if executiontype:
            data['executiontype'] = executiontype
        if status:
            data['status'] = status
        return self.server.tl.updateTestCase(data)

    def createBuild(self, testplanid, buildname, buildnotes=''):
        data = {"devKey": self.devKey,
                "testplanid": testplanid,
                "buildname": buildname,
                "buildnotes": buildnotes}
        return self.server.tl.createBuild(data)

    def createTestCase(self, testcasename, testsuiteid, testprojectid, authorlogin, summary, steps, executiontype=2):
        data = {"devKey": self.devKey,
                "testcasename": testcasename,
                "testsuiteid": testsuiteid,
                "testprojectid": testprojectid,
                "authorlogin": authorlogin,
                "summary": summary,
                "steps": steps,
                "executiontype": executiontype}
        return self.server.tl.createTestCase(data)

    def createTestSuite(self, testprojectid, testsuitename, details=''):
        data = {"devKey": self.devKey,
                "testprojectid": testprojectid,
                "testsuitename": testsuitename,
                "details": details}
        return self.server.tl.createTestSuite(data)

    def createTestPlan(self, testplanname, testprojectname, notes='', active=2, public=2):
        data = {"devKey": self.devKey,
                "testplanname": testplanname,
                "testprojectname": testprojectname,
                "notes": notes,
                "active": active,
                "public": public}
        return self.server.tl.createTestPlan(data)

    def createTestProject(self, testprojectname, testcaseprefix):
        data = {"devKey": self.devKey,
                "testprojectname": testprojectname,
                "testcaseprefix": testcaseprefix}
        return self.server.tl.createTestProject(data)

    def uploadExecutionAttachment(self, executionid, filename, filetype, content, title, description):
        data = {"executionid": executionid,
                "devKey": self.devKey,
                "filename": filename,
                "filetype": filetype,
                "content": content,
                "title": title,
                "description": description}
        return self.server.tl.uploadExecutionAttachment(data)

    def reportTCResult(self, testcaseid, testplanid, status, buildid, platformname, execduration, steps, notes=''):
        data = {"devKey": self.devKey,
                "testcaseid": testcaseid,
                "testplanid": testplanid,
                "notes": notes,
                "status": status,
                "buildid": buildid,
                "platformname": platformname,
                "execduration": execduration,
                "steps": steps}
        return self.server.tl.reportTCResult(data)

    def getProjects(self):
        data = {"devKey": self.devKey}
        return self.server.tl.getProjects(data)

    def getTestPlanByName(self, testprojectname, testplanname):
        data = {"devKey": self.devKey,
                "testprojectname": testprojectname,
                "testplanname": testplanname}
        return self.server.tl.getTestPlanByName(data)

    def getProjectTestPlans(self, project_id):
        data = {"devKey": self.devKey, "testprojectid": project_id}
        return self.server.tl.getProjectTestPlans(data)

    def getTestPlanPlatforms(self, testplanid):
        data = {"devKey": self.devKey,
                "testplanid": testplanid}
        return self.server.tl.getTestPlanPlatforms(data)

    def getBuildsForTestPlan(self, testplanid):
        data = {"devKey": self.devKey,
                "testplanid": testplanid}
        return self.server.tl.getBuildsForTestPlan(data)

    def getTestCaseIDByName(self, tc_name, ts_name='', tp_name='', tc_path=''):
        data = {"devKey": self.devKey, "testcasename": tc_name}
        if ts_name:
            data["testsuitename"] = ts_name
        if tp_name:
            data["testprojectname"] = tp_name
        if tc_path:
            data["testcasepathname"] = tc_path
        return self.server.tl.getTestCaseIDByName(data)

    def getTestCase(self, testcaseid):
        data = {"devKey": self.devKey,
                "testcaseid": testcaseid}
        return self.server.tl.getTestCase(data)

    def getTestProjectByName(self, testprojectname):
        data = {"devKey": self.devKey,
                "testprojectname": testprojectname}
        return self.server.tl.getTestProjectByName(data)

    def getTestSuitesForTestPlan(self, testplanid):
        data = {"devKey": self.devKey,
                "testplanid": testplanid}
        return self.server.tl.getTestSuitesForTestPlan(data)

    def getTestPlanByName(self, testprojectname, testplanname):
        data = {"devKey": self.devKey,
                "testprojectname": testprojectname,
                "testplanname": testplanname}
        return self.server.tl.getTestPlanByName(data)

    def getInfo(self):
        return self.server.tl.about()
