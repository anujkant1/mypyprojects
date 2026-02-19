"""
Simple random event simulation: packet loss simulation. Consider the case that a sender sends a list of data packets one by one through an unreliable network to a reciver sequentially. Each packet being sent may be lost or corrupted with a fixed probability of 40% and hence won't be collected by the receiver. Write a function to simulate the packet loss random event by taking a list and lost probability and return the collected(i.e., uncorrupted) data as a list.

Bonus question: If we repeat the same simulation many times with the same input list and fixed loss probability, what is the expected length of the output list? What distribution the output length will be? Any other approaches to simulate the same event (e.g., binomial masking)?
"""

import random
data_packets = [1,2,3,4,5,6,7,8,9,10]
loss_probability = 0.4

def simulate_packet_loss(data_packets, loss_probability):
    collected_packets = []
    for packet in data_packets:
        if random.uniform(0.0, 1.0) > loss_probability:
            collected_packets.append(packet)
    return collected_packets

print(simulate_packet_loss(data_packets, loss_probability))