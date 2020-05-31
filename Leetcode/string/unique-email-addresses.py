class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for index, email in enumerate(emails):
            email = email.split('@')[0].split('+')[0].replace(".","") +'@'+ email.split('@')[1]
            emails[index] = email
            
        #print(emails)
        emails[:] = list(set(emails))
        
        return len(emails)
        
            
        