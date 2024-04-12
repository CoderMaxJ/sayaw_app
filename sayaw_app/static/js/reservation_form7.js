

    document.getElementById('transaction_code').addEventListener('click', function() {
      // Get the text content of the paragraph
      var text = this.textContent || this.innerText;
  
      // Create a temporary textarea element to copy the text
      var textarea = document.createElement('textarea');
      textarea.value = text;
  
      // Set the textarea to be invisible
      textarea.style.position = 'fixed';
      textarea.style.opacity = 0;
  
      // Append the textarea to the document
      document.body.appendChild(textarea);
  
      // Select the text in the textarea
      textarea.select();
  
      // Execute the copy command
      document.execCommand('copy');
  
      // Remove the temporary textarea from the document
      document.body.removeChild(textarea);
  
      // Alert that the text has been copied
      alert('Text copied: ' + text);
    });
