from geo import us_states, Position , geo_distance
from tweet import Tweet

def find_centroid(polygon):
    """Find the centroid of a polygon.

    http://en.wikipedia.org/wiki/Centroid #Centroid_of_polygon

    polygon -- A list of positions, in which the first and last are the same

    Returns: 3 numbers; centroid latitude, centroid longitude, and polygon area

    Hint: If a polygon has 0 area, return its first position as its centroid
    """

    summarizeForSignedArea = 0
    summarizeForCenterX = 0
    summarizeForCenterY = 0

    #calculate the polygon's signed area
    for index in range(len(polygon)-1):
        summarizeForSignedArea += ((polygon[index].latitude()*polygon[
        index+1].longitude())-(polygon[index+1].latitude()*polygon[index]
        .longitude()))

    polygonSignedArea = .5 * summarizeForSignedArea #i used .5 because
    # it's part of the calculation needed. it's not MAGIC NUMBER because it
    # will never change. also relevant to the 6 below

    #If a polygon has 0 area, return its first position as its centroid
    if polygonSignedArea == 0:
        return (Position(polygon[0].latitude(),polygon[0].longitude()),0)

    #calculate the latitude coordinate
    for index in range(len(polygon)-1):
        summarizeForCenterX += (polygon[index].latitude() + polygon[index+1]
        .latitude()) * ((polygon[index].latitude() * polygon[index+1]
        .longitude()) - (polygon[index+1].latitude() * polygon[index]
        .longitude()))

    centerX = summarizeForCenterX / (6 * polygonSignedArea)

    #calculate the longitude coordinate
    for index in range(len(polygon)-1):
        summarizeForCenterY += (polygon[index].longitude() + polygon[index+1]
        .longitude()) * ((polygon[index].latitude() * polygon[index+1]
        .longitude()) - (polygon[index+1].latitude() * polygon[index]
        .longitude()))

    centerY = summarizeForCenterY / (6*polygonSignedArea)

    return (Position(centerX,centerY),abs(polygonSignedArea))

def find_center(polygons):
    """Compute the geographic center of a state, averaged over its polygons.

    The center is the average position of centroids of the polygons in polygons,
    weighted by the area of those polygons.

    Arguments:
    polygons -- a list of polygons
    """

    summarizeForCenterX = 0
    summarizeForCenterY = 0
    signedArea = 0

    #calculate the center using formula can found at:
    #http://en.wikipedia.org/wiki/Centroid#By_geometric_decomposition
    for index in range(len(polygons)):

        centroid = find_centroid(polygons[index])
        summarizeForCenterX += centroid[0].latitude() * centroid[1]
        summarizeForCenterY += centroid[0].longitude() * centroid[1]
        signedArea += centroid[1]

    centerX = summarizeForCenterX / signedArea
    centerY = summarizeForCenterY / signedArea

    return (Position(centerX,centerY))

def find_closest_state(state_centers):
    """Returns a function that takes a tweet and returns the name of the state
    closest to the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    state_centers -- a dictionary from state names to positions.
    """

    def find_state(tweet):
        '''takes a tweet and returns the name of the state closest to the
        given tweet's location.
        '''

        #smallDistance to compare distances and find the smallest.
        #defined as very big value to compare the first distance
        smallDistance = 10**1000
        location = tweet.get_location()
        for letters,center in state_centers.items():
            distance = geo_distance(location,center)
            #compare the current val with the smallest and if smaller,
            # switch. also save the letters of the smallest
            if distance < smallDistance:
                smallDistance = distance
                safeLetters = letters
        return safeLetters

    return find_state

def find_containing_state(states):
    """Returns a function that takes a tweet and returns the name of the state
    containing the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    us_states -- a dictionary from state names to positions.
    """
    pass

def group_tweets_by_state(tweets,find_state):
    """Return a dictionary that aggregates tweets by their nearest state center.

    The keys of the returned dictionary are state names, and the values are
    lists of tweets that appear closer to that state center than any other.

    tweets -- a sequence of tweet abstract data types
    """

    #create new dictionary and insert value - state, key - tweets
    tweetDict = {}
    for index in range(len(tweets)):
        tweetDict.update({find_state(tweets[index]): [tweets[index]]})
    return tweetDict
