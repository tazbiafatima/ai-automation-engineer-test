# Assignment: Audience optimization tool

![Assignment repo banner](img/assignment_banner.webp)

## Objective

Develop a script that generates headline, SEO URL and social media post suggestions for Hearst Newspaper content using OpenAI's API. In addition, provide a risk analysis and mitigation strategies for automated content suggestions.

### Assignment details

- **Duration:** 1 hour and 30 minutes (Zoom call with Ryan Serpico)
- **OpenAI API key:** Ryan Serpico will provide you with a temporary OpenAI API key. He will delete the key after your time is up.
- **Sample Articles:** Located in the `/data` folder. Use these to demonstrate your knowledge of few-shot prompting. Use `test_article.txt` to test your script.
- **Submission:** Provide a link to a GitHub repository with your code. Exclude the API key from your submission.

---

## Part 1: Coding challenge

### Task

Create a Python (or JavaScript) program that:

1. Interfaces with OpenAI's API (you should use the `GPT-4o` model).
2. Generates the following suggestions for given article text:
   - Headline
   - SEO URL
   - Social media post

### Final product expectations

- **Input:** The program should accept articles in the form of plain text via terminal.
- **Output:** The program should print suggestions in the terminal in *JSON format*.

### What we're looking for

- **Prompt Structure:** Each API call must include:
  - *One* system message
  - *At least* one human message
  - *At least* one AI message
- **Few-Shot Prompting:** Demonstrate your knowledge of this concept. Use the sample articles.
- **Tone:** Match the tone of prior articles from the San Francisco Chronicle.
- **Determinism:** Strive for consistent responses (fully deterministic output is not required).

### Optional

- **Framworks:** Feel free to use any libraries or frameworks you're comfortable with (LangChain, DSPy, etc.).

### What not to do

- Do not create a UI.
- Do not create a conversational chatbot.

---

## Part 2: Risk Analysis and mitigation strategies

### Task

Describe potential risks and challenges associated with automated content suggestions for news articles. Consider:

- Accuracy of generated content
- Handling of sensitive or controversial topics
- Dependence on the AI model's understanding of context

### Requirements

- **Word Count:** Approximately 300 words

---

## Part 3: Explanation of ChatGPT/Github Copilot Use (*Optional*)

### Task

It's 2024. Anyone can just ask ChatGPT and/or Github Copilot to complete coding assignments for them. Don't you dare!

Just kidding. I use ChatGPT and Github Copilot every day. These tools have dramatically raised the ceiling of my capabilities. It'd be weird if I judged you for using it in this assignment.

My only request is that you be honest. If you used an AI tool like ChatGPT, Copilot or even Devin, please tell me how you used it! Share your prompts and your approach. I would love to see how you incorporate these tools into your work.

If you don't use these tools at all for this assignment, feel free to blow off this part and submit your assignment!

---

Feel free to reach out if you have any questions. Good luck!
