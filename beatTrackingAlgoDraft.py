
def TempoInduction():
    #initialize 
    foundK= false
    clusterWidth = 0 #define clusterWidth
    IOI = [ [0]*len(eventList) for i in range(len(eventList))] #2d array of size eventList x eventList
    clusterList = [] #pass in a list of clusters, where each clsuter has an interval, score, and size
    eventList = [] #get from some feature extraction
    n = 0 #define some value here
    relationshipFactor =  RelationshipFactor(d) #define relationship factor f(n), look up what d is
    #algorithm
    for event1Index in range(len(eventList)):
        for event2Index in range(len(eventList)):
            IOI[event1Index][event2Index] = math.abs(event2Index.onset - event1Index.onset)
            for cluster in clusterList:
                if math.abs(cluster.interval - IOI[event1Index][event2Index]) < clusterWidth: #what does it mean by is minimum
                    cluster = cluster.union(IOI[event1Index][event2Index])
                    foundK = true
                if !foundK:
                    #create new cluster st cluster = IOI[event1Index][event2Index]
                    clusterList.append(cluster)
    for i in range(len(clusterList)):
        for j in range(len(clusterList)):
            if clusterList[i] != clusterList[j]:
                if math.abs(clusterList[i].interval - clusterList[j].interval) < clusterWidth:
                    clusterList[i] = clusterList[i].union(clusterList[j])
                    del clusterList[j] #delete jth cluster
    for i in range(len(clusterList)):
        for j in range(len(clusterList)):
            if math.abs(clusterList[i] - n * clusterList[j]) < clusterWidth:
                clusterList[i].score = clusterList[i].score + relationshipFactor * clusterList[j].size
                
def RelationshipFactor(d):
    if d >= 1 and d <= 4:
        return 6 - d
    if d >= 5 and d <= 8:
        return 1
    return 0
    
    
def BeatTracking(hypothesisCluster):
    #variables
    tempoGuesses = hypothesisCluster # ? input should be a list of predictions for tempo from inner-onset intervals
    eventList = [] #get access to each event
    startupPeriod = 0 #figure out how to define
    agentList = []
    timeOut = 0 #define
    #initialization 
    for guess in tempoGuesses:
        for event in eventList:
            If event.onset < startupPeriod：
                agent = Agent() #what datatype is this?They don’t even say…idea: make my own class
                agent.beatInterval = guess
                agent.prediciton = event.onset + guess
                agent.history = #lookup def of agent
                agent.score = agent.salience #lookup
                agentList.append(agent)
    for eIndex in range(len(eventList)):
        for aIndex in range(len(agentList)):
            if eventList[eIndex].onset - agentList[aIndex].history.last > timeOut:
                del agentList[aIndex]
            while agentList[aIndex].prediction # + T ol_post < eventList[eIndex].onset:
                agentList[aIndex].prediction = agentList[aIndex].prediction + agentList[aIndex].beatInterval
            #finish later when I understand what T ol_pre and T ol_post are
                
class Agent:
    beatInterval = None
    prediciton = None
    history = None #lookup def of agent
    score = None
    salience = None #lookup, can define based off of salience definitions on page 20 