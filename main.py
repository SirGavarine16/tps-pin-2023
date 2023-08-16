# Table 1 = [src, dst, tmsp]
# Table 2 = [dst, tmsp, is_spam]
# Table 3 = [dst, src, spam_count]

from datetime import datetime

def getTimestampDifference(timestamp1, timestamp2):
    parsedTimestamp1 = datetime.strptime(timestamp1, '%Y-%m-%d %H:%M:%S')
    parsedTimestamp2 = datetime.strptime(timestamp2, '%Y-%m-%d %H:%M:%S')
    return abs(parsedTimestamp1 - parsedTimestamp2)

def findSource(table1, destination, timestamp):
    rowsToCheck = [row for row in table1 if row[1] == destination]
    for row in rowsToCheck:
        source = row[0]
        timestampDifference = getTimestampDifference(row[2], timestamp)
        if timestampDifference <= 2:
            return source
    return None

def getSpamRecordIndex(table, destination, source):
    for i in range(len(table)):
        if table[i][0] == destination and table[i][1] == source:
            return i
    return None

def generateSpamDatabase(table1, table2):
    table3 = []
    for row in table2:
        isSpam = row[2]
        if isSpam:
            reporter = row[0]
            timestamp = row[1]
            source = findSource(table1, reporter, timestamp)
            if source:
                index = getSpamRecordIndex(reporter, source)
                if index:
                    table3[index][2] += 1
                else:
                    table3.append([reporter, source, 1]) 
    return table3
