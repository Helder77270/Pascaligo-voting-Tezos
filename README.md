# Pascaligo-voting-Tezos
 A simple vote contract / School Project🗳️

 Objectives:
    Create a smart voting contract in PascalLigo language:

- A user can vote by saying "yes"(vote(True)) 😃 or "no" 😠 (vote(False))
- All users can vote except the owner of the contract 
- A user can only vote once 🥇
- The "administrator" is the owner of the contract. He is defined when we deploy the contract.
- The smart contract is paused when 10 people has voted
- When the smart contract is paused, the result of the vote must be available in the storage 🏪
- The owner can reset, pause and resume the vote ❗
- The smart contract should have unit tests 📝

How to use :

We assume that you already have set your environement, else you can find it by following the links below:

- https://tezos.gitlab.io/introduction/howtoget.html#build-from-sources
- https://ligolang.org/docs/intro/installation/

Step 1 : Compiling your contract 💻

As the unit test is waiting for a file called "voteContract.tz", which is the result of the compiled contract we have to do :

ligo compile-contract votingContract.ligo main > votingContract.tz

The general form of this line is :

ligo compile-contract <your ligo file> <entrypoint> > <name of your .tz file>

Step 2 : Simulation 🔬

To simulate the contract you can use this command below:

ligo dry-run --sender=tz1VPFYwwtWZ5ytH5ZcMYyvqi9AmiR3d8sJT vote.ligo main 'SetAdmin(("tz1VPFYwwtWZ5ytH5ZcMYyvqi9AmiR3d8sJT":address))'  'record votes=map ("tz1VPFYwwtWZ5ytH5ZcMYyvqi9AmiR3d8sJT":address) -> True;end; owner=("tz1VPFYwwtWZ5ytH5ZcMYyvqi9AmiR3d8sJT":address); contractPause=False;yes=0;no=0;end'

If it returns :

( list[] , record[contractPause -> false , no -> 0 , owner -> @"tz1VPFYwwtWZ5ytH5ZcMYyvqi9AmiR3d8sJT" , votes -> map[@"tz1VPFYwwtWZ5ytH5ZcMYyvqi9AmiR3d8sJT" -> true] , yes -> 0] )

Then it worked, else you made an error copying it ! (I've tested it before pushing ) 😄

Step 3 : Run unit tests 🏃‍♂️ 🏃‍♀️

It's the most easy part, you only have to do the command below:

pytest UnitTest.py

You should see that : 

============================================================================================= 4 failed, 4 passed in 2.50s ============================================================

That's the expected result ! 💯

Questions / Help

I would be more than happy to help you, if you need it ! Science is the freer asset to share ! 

🆓🆓🆓 Use this project freely 🆓🆓🆓