import os
import requests
import pdfplumber

url = 'https://www.wgu.edu/content/dam/western-governors/documents/programguides/2017-guides/it/BSCS.pdf'

# download PDF
myfile = requests.get(url)

path = 'C:/Users/Admin/Downloads/BSCS.pdf' 

# translate PDF into 1 big array of words
expectedClasses = [
    'Introduction to IT', 'Applied Probability and Statistics', 'Web Development Foundations',
    'Introduction to Geography', 'Network and Security - Foundations', 'Calculus I',
    'English Composition I', 'Scripting and Programming - Foundations', 'Integrated Physical Sciences',
    'Discrete Mathematics I', 'Discrete Mathematics II', 
    'Introduction to Communication', 'Computer Architecture', 'Scripting and Programming - Applications',
    'Data Management - Foundations', 'Data Management - Applications', 'American Politics and the US Constitution',
    'Introduction to Humanities', 'Software I', 'Software II - Advanced Java Concepts', 
    'Business of IT - Project Management', 'Data Structures and Algorithms I', 'Data Structures and Algorithms II',
    'Ethics in Technology', 'Fundamentals of Information Security', 'Operating Systems for Programmers', 
    'Software Engineering', 'Business of IT - Applications', 'Advanced Data Management',
    'IT Leadership Foundations', 'Technical Communication', 'Introduction to Artificial Intelligence',
    'Software Quality Assurance', 'Computer Science Capstone'    
]

print('\n')
print("WGU Computer Science degree - PDF program guide's page 6 text : ")
print('\n\n')
# PDF's text to compare against
pdf = pdfplumber.open(path)
page = pdf.pages[5]
currentProgramDoc = page.extract_text()
print(currentProgramDoc)
pdf.close()
print('\n\n\n\n')
# run loop to find each class I expect to see
    #return ** Missing ** Class Name if it isn't on there 


# show classes we're looking for
print('Classes expecting to find in this program guide, which were on a previous program guide: \n\n')
print(expectedClasses)
print('\n\n\n\n')


#compare the two and show results
print('Here is the result of the comparison: \n\n')
for x in expectedClasses:
    if currentProgramDoc.find(x) > -1:
        print('+++ ' + x + ' - Found +++')
    else:
        print('######### ' + x + ' - Not found #########')
print('\n\n')




