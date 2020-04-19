# run this test (from tests directory):
# pytest pytest_template.py
# run all tests (from project directory):
# pytest tests

from os.path import dirname, join
from unittest import TestCase
from pytezos import ContractInterface

wallet1     = "tz1dFibFVfuWLBVJHSGrneVFKimuJauc5rEV"
wallet2     = "tz1ajkFrcXfHAXJm8yK8s7mamwth9u4ajzjw"
wallet3     = "tz1VtUMXUwuAfN4euuGg6YC23QT5WDk94M74"
wallet4     = "tz1fPexY96eBrdzXySYzyqq6vM2ZpN5e4q2g"
wallet5     = "tz1LuiwRnA63anqr6ot86xJR3VK86qJxURDj"
wallet6     = "tz1gzyiEoqCCoNjUpmJA1Z21cSf1VzS61E89"
wallet7     = "tz1fssLLW3K822LGaH219oF9ZF8FW8izZXRH"
wallet8     = "tz1fDYG7TcBXBMRfoB5QEtXqF1YunSo17aeo"
wallet9     = "tz1iWiN1hqFHEJEGW4gunUW6o2t1SC8sJoKT"

owner       = "tz1LKe9GQfF4wfob11YjH9grP1YdEWZtPe9W"
wallet10    = "tz1PJSVnbr8ztVSrT2NuBEmGubnYKcxk3zie"

class CounterContractTest(TestCase):

    @classmethod
    def setUpClass(cls):
        project_dir = dirname(dirname(__file__))
        cls.mycontract = ContractInterface.create_from(join(project_dir, 'ligoproject/voteContract.tz'))

    def test_voteAsAnowner(self):
        # Should Fail - failwith("You are an owner")#
        result = self.mycontract.vote(True).result(
            storage={
            "owner": owner,
            "contractPause":  False,
            "votes":  {  },
            "yes": 0,
            "no": 0
            }, source = owner    
        )
           
    def test_noDoubleVote(self):
        # Should Fail - failwith("You have already voted")#
        result = self.mycontract.vote(True).result(
            storage={
            "owner": owner,
            "contractPause":  False,
            "votes":  { wallet1: True },
            "yes": 0,
            "no": 0
            }, source = wallet1
        
        )

    def test_voteCounterYes(self):
        result = self.mycontract.vote(True).result(
            storage={
            "owner": owner,
            "contractPause":  False,
            "votes":  { },
            "yes": 0,
            "no": 0
            }, source = wallet1
            
        )
        self.assertEqual(1, result.storage["yes"])
        
    def test_voteCounterNo(self):
        # Should Fail #
        result = self.mycontract.vote(False).result(
            storage={
            "owner": owner,
            "contractPause":  False,
            "votes":  { },
            "yes": 0,
            "no": 0
            }, source = wallet1
            
        )
        self.assertEqual(1, result.storage["no"])

    def test_votePauseLimit(self):
        result = self.mycontract.vote(True).result(
        storage = {
            "owner": owner,
            "contractPause": False,
            "votes": { wallet1: True},
            "yes": 4,
            "no": 6
        },source = wallet2

        )
        self.assertEqual(10, result.storage['yes'] + result.storage['no'])
        self.assertEqual(True, result.storage['contractPause'])
    
    def test_votePauseIsTrueWhen10Vote(self):
        result = self.mycontract.vote(True).result(
        storage = {
            "owner": owner,
            "contractPause": False,
            "votes": { wallet1: True},
            "yes": 4,
            "no": 5
        },source = wallet2

        )
        self.assertEqual(True, result.storage['contractPause'])

    def test_resetIfNotowner(self):
        # Should fail - failwith("[owner] You need owner privileges to run this .");
        result = self.mycontract.reset(None).result(
        storage = {
            "owner": owner,
            "contractPause": False,
            "votes": { wallet1: True},
            "yes": 4,
            "no": 6
        },
        source = wallet5
        )

    def test_resetIfowner(self):
        result = self.mycontract.reset(None).result(
        storage = {
            "owner": owner,
            "contractPause": True,
            "votes": { wallet1: True},
            "yes": 4,
            "no": 6
        },
        source = owner
        )
