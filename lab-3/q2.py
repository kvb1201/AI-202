# Design a Simple Reflex Agent for an Indian Railways Level Crossing. The agent must
# ensure maximum safety for road traffic while minimizing delays for the train, using
# multi-source sensory input without historical tracking.
# The environment consists of a double-track railway line intersecting a busy state
# highway. The percepts include the following:
# ● Track Sensors (Inbound/Outbound): Sensors placed 2km away that detect if a
# train is currently passing over them. It is either detected or not detected.
# ● Obstacle Sensors (Yellow Box): A grid of sensors on the road between the gates
# to detect “stuck” vehicles (e.g., an auto-rickshaw or buffalo).
# ● Manual Emergency Input: A physical lever for the station master. It is either
# Neutral or Active.
# Actuators:
# ● Gate Arm: Lower/Raise
# ● Hooter/Siren: On/Off
# ● Signal to Train: Green (Safe to proceed)/Red (Emergency Stop)

# Design the rules set. Show the simulation output with percept, action, and location. Do you need
# priorities in the rules?





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
    (False, False, False, False),  # Normal condition
    (True,  False, False, False),  # Train approaching
    (True,  False, True,  False),  # Obstacle detected with train
    (False, False, False, True),   # Manual emergency override
    (False, False, False, False)   # Back to normal
]

print("---- Simulation Output ----")

for t, step in enumerate(simulation_steps):
    # Update environment percepts
    env.inbound_track, env.outbound_track, env.obstacle, env.manual = step

    # Agent perceives environment
    percept = agent_obj.perceives(
        env.inbound_track,
        env.outbound_track,
        env.obstacle,
        env.manual
    )

    # Agent selects action based on current percept
    action = agent_obj.action(*percept)

    # Environment applies action
    env.change(action)

    # Display current state
    print(
        f"t{t} | "
        f"Percept: (In={env.inbound_track}, Out={env.outbound_track}, "
        f"Obs={env.obstacle}, Manual={env.manual}) | "
        f"Action: (Barrier={'CLOSED' if env.barrier else 'OPEN'}, "
        f"Signal={env.signal}, Siren={'ON' if env.siren else 'OFF'})"
    )

    
