
#Copyright 2019 D-Wave Systems Inc.
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



#  STORY NOTES:                                        ***
#  :
#
# Classroom with 30 desks. Due to recent COVID need to social distance now.
#
# The room had 6 rows and 5 desks a row. Made a wide center ailse, 
# (arrive by sides,leave by centre ailse)  so now have
# 2 blocks of 3 x 5. Each can de considered independantly due to ailse spacing.
#
# Constraints: No adjacent students. Front or back or kitty corner.
# Q How may students can a block hold. How many empty desks. Percent Occupany.
# How many more classrooms / teachers needed if school originally had
# 300 students/ 10 teachers. Seating configuration maps for 1 block. 
  

import datetime
import networkx as nx
import dwave_networkx as dnx

import matplotlib.pyplot as plt
from dwave.system.samplers import DWaveSampler

from dwave.system.composites import EmbeddingComposite


sampler = EmbeddingComposite(DWaveSampler())

#CONSTRAINTS
# 3 x 3  on 3 row generator.

G = nx.Graph()


                                                    
G.add_edges_from ([(1, 2 ),(2, 3 ),(3, 4 ),(4, 5 ),(6, 7 ),(7, 8 ),(8, 9 ),(9, 10 ),(1, 6 ),(2, 7 ),(3, 8 ),(4, 9 ),(5, 10 ),(1, 7 ),(2, 8 ),(3, 9 ),(4, 10 ),(2, 6 ),(3, 7 ),(4, 8 ),(5, 9 ),(11, 12 ),(12, 13 ),(13, 14 ),(14, 15 ),(6, 11 ),(7, 12 ),(8, 13 ),(9, 14 ),(10, 15 ),(6, 12 ),(7, 13 ),(8, 14 ),(9, 15 ),(7, 11 ),(8, 12 ),(9, 13 ),(10, 14 )])
                   
                
S = dnx.maximum_independent_set(G, sampler=sampler, num_reads = 10)

                  

#   adjust your  printout requirments ---------------REPORT---------***
timestamp = datetime.datetime.now()
print(" ")
print("--------------------------------------------------------------")
print("")
print("Run                             ",timestamp)
print("--------------------------------------------------------------")
print("Total avaiable seats - nodes  15 in each section "),
print("Maximum  set size     ", len (S))
print("Missed ", 15 -len(S))
print("Assignments in Nodes this run   ",S)
print("--------------------------------------------------------------")
print(" ")
k =G.subgraph(S)
notS =list(set(G.nodes())-set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G,pos=pos)
nx.draw(k,pos=pos)
nx.draw(othersubgraph,pos=pos,node_color ='b')
plt.show()
