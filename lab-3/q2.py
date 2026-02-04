
"""
Rules:
1. Manual emergency override: Signal-Red, Activate the siren, gate closed
2. Obstacle detected: Signal-Red, siren on, gate closed
3. Train on any track, no obstacle: signal-green, siren on, gate closed
4. No trains: Signal green, siren off, gate open
"""

#rules stores priority and environment changes , more priority action first
#barrier,signal,siren
rules ={"MANUAL_OVERRIDE": (True, "RED", True),
        "OBSTACLE":(True,"RED",True),
        "TRAIN":(True,"GREEN",True),
        "NO TRAIN": (False,"GREEN",False)
}



class agent:

    def __init__(self):
        pass

    def perceives(self,inbound_track, outbound_track, obstacle, manual):
        return (inbound_track,outbound_track,obstacle, manual)
    
    def action(self,inbound_track,outbound_track,obstacle, manual):
        if manual:
            return rules["MANUAL_OVERRIDE"]
        if obstacle:
            return rules["OBSTACLE"]
        if inbound_track or outbound_track:
            return rules["TRAIN"]
        else:
            return rules['NO TRAIN'] 
    




class environment:

    def __init__(self):

        # False on track means no train detected
        # False barrier means barrier is OPEN
        # True barrier means barrier is CLOSED
        self.inbound_track = False  
        self.outbound_track = False 
        self.obstacle = False
        self.manual = False
        self.signal = "GREEN"
        self.siren = False
        self.barrier = False 

    def change(self, action):
        barrier,signal,siren = action
        self.barrier = barrier
        self.signal = signal
        self.siren = siren
        







agent_obj = agent()
env = environment()

# Each tuple: (inbound_track, outbound_track, obstacle, manual)
simulation_steps = [
    (False, False, False, False),  # normal condition
    (True,  False, False, False),  # train approaching
    (True,  False, True,  False),  # obstacle detected with train
    (False, False, False, True),   # manual emergency override
    (False, False, False, False)   # back to normal
]

print("---- Simulation Output ----")

for t, step in enumerate(simulation_steps):

    env.inbound_track, env.outbound_track, env.obstacle, env.manual = step


    percept = agent_obj.perceives(
        env.inbound_track,
        env.outbound_track,
        env.obstacle,
        env.manual
    )


    action = agent_obj.action(*percept)

    env.change(action)

    print(
        f"t{t} | "
        f"Percept: (In={env.inbound_track}, Out={env.outbound_track}, "
        f"Obs={env.obstacle}, Manual={env.manual}) | "
        f"Action: (Barrier={'CLOSED' if env.barrier else 'OPEN'}, "
        f"Signal={env.signal}, Siren={'ON' if env.siren else 'OFF'})"
    )

    
