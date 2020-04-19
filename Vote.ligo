type storage is record
    owner:address;
    contractPause: bool;
    votes: map(address, bool);
    yes:int;
    no:int;
end

type action is
| SetAdmin of address
| Pause of bool
| Vote of bool
| Reset of unit

function isAdmin (const s : storage) : bool is
  block {skip} with (sender = s.owner)

function isPaused (const s : storage) : bool is
  block{skip} with (s.contractPause)

function setPause (const s : storage; const setter : bool) : storage is
  block{
      s.contractPause := setter
    } with s

function setadm (const s : storage ; const addr : address) : storage is
   block { 
      if(isAdmin(s)) 
       then s.owner := addr 
        else failwith("[ADMIN SET ERROR]You can't set an admin");
   } with s

function reset(const s : storage) : storage is
 block {
    if ( isAdmin(s) )
      then block {
        if ( isPaused(s) )
          then block {
            for i in map s.votes block {
              remove i from map s.votes;
            };
           s := setPause(s,False)
          }
          else block {
            failwith("[RESET ERROR] Vote contract in its paused state.");
          }
      }
      else block {
        failwith("[RESET ERROR] You need admin privileges to run this .");
      }
  } with s


function vote(const s : storage ; const vote : bool) : storage is
  block{
    if( isPaused(s) = False ) 
     then block {
      if( isAdmin(s) = False) 
       then block {
        case s.votes[sender] of
           Some(bool) -> failwith("[VOTING ERROR] You have already voted")
          | None -> block {
            s.votes[sender] := vote;
              if(vote) then block{
                s.yes := s.yes + 1;
              } else s.no := s.no + 1;
              
                if((s.yes + s.no) = 10) then block{
                  s := setPause(s,True);
                }else block { skip }               
            }
        end;
      } else failwith("[VOTING ERROR] You are an admin")
    } else failwith("[VOTING ERROR] Contract is paused")
  } with s
 

function main (const p : action ; const s : storage) : (list(operation) * storage) is
  block { s.owner := sender } with ((nil : list(operation)),
  case p of
  | Pause(b) -> setPause(s, b)
  | SetAdmin(a) -> setadm(s, a)
  | Vote(c) -> vote(s, c)
  | Reset -> reset(s)
  end)