"""
Made By Learn Build Share
"""

# Parameters = Variables in the function definition.
# Arguments = Actual values in the function call.
def analyze_resume(resume, job_role):
    """ 
    Parameter::
    resume: str: The text content of the resume to be analyzed.
    job_role: str: The job role for which the resume is being analyzed.
    """
    print("Analyzing Resume...")
    print("Resume:", resume)
    print("Job Role:", job_role)


# Function Call
analyze_resume("resume.pdf", "Python Developer")
analyze_resume("resume.pdf", "Java Developer")
analyze_resume("resume.pdf", "Data Science Developer")



