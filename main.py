# Import the wikipedia module
import wikipedia

# define the function to pass the keywords as arguments
def search(*args):
    # search for the given parameters

    # result = wikipedia.search(*args) # output will be in list

    # result = wikipedia.suggest(*args) # to get suggestion

    # result = wikipedia.geosearch(**kwargs) #geosearch feature allows you to search for articles that are geographically related to a specific location.

    #You can use the wikipedia.page() function to get the contents of a specific Wikipedia page
    # result = wikipedia.page(*args)
    # print(result.title) # to get title
    # print(result.url) # to get url
    # print(result.content[:500]) # to get 500 words content
    result = wikipedia.summary(*args)
    print(result)


search(input("Enter You word: "))
