# Resume-Parser
A  comprehensive resume parser, capable of extracting detailed information from resumes in various formats (PDF, JPG, HTML, DOC, etc.). The parser accurately classify text into distinct sections (e.g., education, work experience, skills) and sequence them based on dates, where available. Also standardize different job titles and occupations against the O-NET database, ensuring a consistent taxonomy across parsed resumes and implement an advanced feature that mines detailed skills and competencies from project descriptions and position roles within the resume, highlighting the candidate's specific abilities and expertise. Abstractive skill extraction is a bonus.

<div align="center">
  
# How it works
</div>

The Resume Matcher takes your resume as input, parses them using Python, and with various libraries and models, analyse all your resume and providing you with detailed information, section classification, job extraction, skill extraction and prediction with json file format.

The process is as follows:

1. **Parsing**: The system uses Python to parse both your resume.

2. **Classification into different section**: The tool uses python script to extract the details with their classess and extract them from your resume. The sections includes e.g.,  Name, email, education, work experience, skills.

3. **Job extraction**: The tool enables to extract job title from input resume and matches with the exixting O*NET database.
   
4. **Skill extraction and prediction**: It also extarct the skill from the resume as it contains projects and jobs and also accouding to it, it can predict the skills that user have. This can be done using 
