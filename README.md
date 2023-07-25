# New Interaction Paradigm for Complex EDA Software Leveraging GPT


## Abstract
In the rapidly evolving field of electronic design automation (EDA), intricate software like KiCad [1] provide extensive design functionalities. However, the intricate command structure and high learning curve create a barrier to entry, particularly for novice printed circuit board (PCB) designers. This results in difficulty in selecting appropriate functions or plugins for varying design purposes, compounded by the lack of intuitive learning methods beyond traditional documentation, videos, and online forums.
To address this challenge, we introduce SmartonAI, an artificial intelligence (AI) interaction helper plugin for KiCad. SmartonAI is inspired by the HuggingGPT framework [2] and employs large language models, such as GPT [3-5] and BERT [6], to facilitate task planning and execution. On receiving a designer request, SmartonAI conducts a task breakdown and efficiently executes relevant subtasks, such as analysis of help documentation paragraphs and execution of different plugins, along with leveraging the built-in schematic and PCB manipulation functions in KiCad.
Our preliminary results demonstrate that SmartonAI can significantly streamline the PCB design process by simplifying complex commands into intuitive language-based interactions. By harnessing the powerful language capabilities of ChatGPT and the rich design functions of KiCad, the plugin effectively bridges the gap between complex EDA software and user-friendly interaction.
In conclusion, SmartonAI not only has the potential to democratize access to EDA software for novices, but also promises to enhance productivity for experienced designers. Its application could extend to other complex software systems, illustrating the immense potential of AI-assisted user interfaces in advancing digital interactions across various domains.
## 1. Introduction and Overview of SmartonAI
### 1.1. Brief description of SmartonAI

SmartonAI, a groundbreaking development by Wisdom Empowerment Technology, revolutionizes electronic circuit design automation. Merging the power of AI with a collaborative multi-model, multi-software simulation environment, it paves the way for an innovative design process for power electronics, particularly important in our energy-conscious era. Composed of a distinguished team from globally renowned institutions, SmartonAI's development is fueled by years of combined experience in power electronics and AI, creating a robust foundation for this transformative initiative.
### 1.2. Explanation of the need for such an AI-assisted interface

In the domain of Printed Circuit Board (PCB) design, traditional learning resources often fall short of providing intuitive and accessible learning pathways, especially for software like KiCad, known for its rich features but steep learning curve. This hurdle can delay efficient onboarding and hinder the swift execution of design tasks, even for those with a foundational understanding of PCB design.
An AI-assisted interface like SmartonAI offers a solution by transforming the way users interact with EDA software. By interpreting natural language commands and conducting task breakdowns, it allows for a high level of personalization and context-aware guidance. This AI-augmentation effectively bridges the knowledge gap, making the vast array of functions and plugins within KiCad more accessible to users.
Such an interface not only democratizes access to advanced EDA software but also optimizes the learning process, fostering a more productive and user-friendly environment. It is these market needs and challenges that have inspired and shaped the development of SmartonAI.
### 1.3. Overview of the two main components of SmartonAI: Chat Plugin and OneCommandLine Plugin

SmartonAI consists of two main components, each contributing significantly to the overall user experience and effectiveness of the system:
1.3.1 Chat Plugin
The Chat Plugin serves as an interactive AI tutor, guiding users through the functionalities related to PCB design (pcbnew) [7] and schematics (eeschema) [8] in KiCad. It is designed to understand user queries, analyze, and break down tasks, and offer solutions in a conversational manner akin to ChatGPT. This feature greatly simplifies the learning curve, providing contextually aware and personalized assistance.
1.3.2 OneCommandLine Plugin
The OneCommandLine Plugin, on the other hand, primarily focuses on plugin selection and intelligent execution based on user needs. By understanding user commands, it facilitates rapid plugin selection and activation, thus speeding up the design process and improving productivity.
Together, these two components empower users with a seamless, intelligent, and highly interactive design environment within KiCad, enhancing both the learning and practical aspects of electronic design automation.

### 1.4 Support languages

Currently, SmartonAI supports both English and Chinese for user interaction. Additionally, the help instructions provided by the Chat Plugin include diagrams in both languages. This enables a broader audience to interact with and benefit from the system more efficiently. Future updates may incorporate other languages based on user demand, further enhancing the inclusivity and usability of the system on a global scale.

## 2. The Chat Plugin in SmartonAI
The Chat Plugin of SmartonAI functions through two major components: The Main-Sub GPT and the Question-Answer (QA) GPT.
### 2.1. Detailed explanation of the Chat Plugin
2.1.1 Main-Sub GPT
In this system, the user initiates the process by entering their query or requirement into the plugin's dialog box. These user inputs are then analyzed by the primary GPT, which identifies the 1-3 most relevant tasks from a pre-classified set of 20. Each of these primary tasks corresponds to a dedicated sub-GPT. The sub-GPTs further interact with the user to determine the most suitable sub-task from their respective domains.
The selected subtasks serve as the foundation to create personalized learning documents that cater to the user's specific needs. Once these documents are generated, they are sent to the QA GPT for further processing.
If the user finds the recommended primary or sub-task unsatisfactory, they are allowed to provide reasons for their dissatisfaction. This feedback mechanism enables users to revisit their choices, ensuring that the system accurately meets their requirements.
2.1.2 Question-Answer GPT
The QA GPT initiates the interaction by providing responses to the user's initial questions or concerns. Users can continue to chat and ask questions, and the QA GPT responds based on the built-in document information and knowledge from the GPT model.
A distinctive feature of the QA GPT is its data augmentation functionality, which comes into play when a user's interaction hits a knowledge bottleneck or when the user wishes to inquire about a different overarching topic. It is capable of reading and learning relevant information from chat logs and integrating this new knowledge into its responses.
### 2.2. Description of how it divides common queries and requirements into 20 main tasks and hundreds of subtasks based on KiCad's official documentation
Our team took a deep dive into KiCad's official help documentation, effectively dissecting it into 20 core tasks that form the main scaffolding of the software's functionalities. These main tasks were then further broken down into more than a hundred subtasks, ensuring a comprehensive and nuanced coverage of the software's operations. This approach, driven by the authoritative guidelines from KiCad itself, ensures a professional, effective, and user-centric division of tasks within the Chat Plugin.
### 2.3. Explanation of how it provides user-specific introductory paragraphs and chat support services based on these tasks and subtasks
The Chat Plugin harnesses the main tasks and subtasks framework to provide user-centric resources and support. We have meticulously decomposed the KiCad official documentation into multiple HTML pages, each corresponding to a particular subtask. Once a user's requirements are mapped to certain subtasks, SmartonAI ingeniously stitches these HTML pages together, enhancing the presentation with CSS and JavaScript for an optimized, user-friendly interface. Users can access this tailored documentation by clicking on the "view result" option.
Moreover, the amalgamated content from these HTML pages forms a pre-set input for the QA GPT, enabling it to answer user queries based on the specific subtask-based context. This structure allows the Chat Plugin to offer a bespoke learning journey for each user, augmenting the effectiveness of the QA GPT in subsequent question-answer sessions.
### 2.4. Description of how it can add additional information based on user feedback

The system is designed to continuously learn and adapt based on user interactions. As users converse with the QA GPT and present unique queries or points of confusion, the system leverages its data augmentation capabilities to gather additional information and integrate it into future responses. This process of continuous feedback and learning ensures that the Chat Plugin remains relevant and adaptive to evolving user needs.

## 3. The OneCommandLine Plugin in SmartonAI
### 3.1. Introduction to OneCommandLine Plugin and Its Core Functionality

Our SmartonAI system is greatly enhanced by the OneCommandLine Plugin, an essential component designed to simplify plugin selection and expedite their execution within KiCad. The user-friendly chat interface of the plugin facilitates direct interaction with the users, providing them with a streamlined and efficient process to accomplish their tasks. 

Initially, we fed our GPT model with predefined descriptions and function specifications of commonly used plugins. This enabled the AI to familiarize itself with the plugins' purpose and functionality, paving the way for the plugin's core operation - intelligent plugin recommendation.

### 3.2. Intelligent Plugin Recommendation System

One of the key features of the OneCommandLine plugin is its ability to recommend plugins based on the user's specific requirements. As users interact with the plugin via the chat interface, it first presents a list of supported plugins. Armed with the descriptions and use-cases we initially defined, the plugin matches the user's needs with these descriptions. As a result, it recommends plugins that best align with the user's objectives, making the process not only efficient but also tailored to the user's unique needs.

### 3.3. Explanation of how it accepts user input to intelligently call plugins

Once the user confirms the selected plugin, the OneCommandLine Plugin provides the necessary parameters and showcases input examples for the chosen plugin. This provides clarity to users on how to proceed with the plugin and its execution.

After users submit their specified parameters, the plugin automates the rest of the process. It automatically calls the corresponding plugin function based on the user-input parameters. Following this, the PCB editor page updates to reflect the changes brought about by the executed plugin function. This update occurs upon the user's subsequent click on the PCB editor page, making for a seamless, efficient, and user-friendly experience.

## 4. The Interaction Between the Chat Plugin and OneCommandLine Plugin
### 4.1. Discussion of how the two plugins work together

The Chat Plugin and OneCommandLine Plugin work together seamlessly, providing a robust and comprehensive solution for users navigating KiCad. The Chat Plugin, designed to assist with learning and understanding the functionalities of KiCad, complements the OneCommandLine Plugin that focuses on the swift selection and deployment of relevant plugins.

When a user poses a query or specifies a requirement, the Chat Plugin kicks into action. It breaks down the user's request into main tasks and subtasks, and based on this analysis, it generates custom learning resources that can help the user navigate their project better. This process leads to a more effective and engaging learning experience for the user.

Simultaneously, the OneCommandLine Plugin utilizes this contextual information from the user's interaction with the Chat Plugin to recommend the most suitable plugins that align with the user's needs. This streamlines the process of plugin selection and further enhances the user's engagement with KiCad.

### 4.2. Illustration of how they enhance user interaction with KiCad

With the synergistic functioning of the Chat Plugin and OneCommandLine Plugin, user interaction with KiCad is significantly enhanced. The intuitive chat-based interface of both plugins introduces an element of interactivity that is often lacking in traditional PCB design software, leading to an enriched user experience.

The tailored learning resources generated by the Chat Plugin empower the user with knowledge, improving their understanding of the KiCad functionalities. This, coupled with the intelligent plugin recommendation system of the OneCommandLine Plugin, reduces the learning curve for users, enabling them to design more efficiently and effectively.

The plugins' ability to respond to user requirements not only makes the design process faster and more efficient but also encourages users to explore the full potential of KiCad. Consequently, this contributes to the goal of SmartonAI to revolutionize the PCB design process, fostering innovation and efficiency in the new era of energy technology.



## 5. Potential Impact and Future Applications
### 5.1. Democratizing Access to EDA Software through SmartonAI

The SmartonAI platform holds immense potential to democratize access to Electronic Design Automation (EDA) software like KiCad. By simplifying the learning curve and providing personalized guidance, SmartonAI makes complex EDA functionalities more accessible to a broader audience. Notably, the advanced AI-driven approach helps beginners get started more quickly and easily, overcoming initial barriers of entry into the world of PCB design.

### 5.2. Enhancing Productivity for Experienced Designers

For experienced designers, SmartonAI can significantly enhance productivity. The intelligent, AI-based interaction can streamline the design process by recommending relevant plugins and automating routine tasks. This leaves more time for designers to focus on creative, high-level design decisions.

Moreover, the OneCommandLine plugin offers the flexibility for designers to add their own defined plugins and descriptions. This enriches the plugin library and paves the way for integrating more functionalities into the design workflow. By doing so, experienced designers can tailor the software to their specific needs, further increasing their efficiency and productivity.

### 5.3. Extending AI-Assisted Approach to Other Complex Software Systems

The AI-assisted approach developed by SmartonAI can potentially be extended to other complex software systems. The core concept of parsing complex tasks into manageable sub-tasks, providing AI-assisted guidance, and enabling plugin customization has wide applicability across various software ecosystems.

Such a system could revolutionize the way users interact with complex software, reducing the learning curve, and enabling more efficient and effective use of these tools. The long-term impact could be a significant enhancement in the productivity and creativity of software users across many fields.

## 6. Conclusion

The implementation of AI-driven solutions in PCB design software, like KiCad, marks a significant leap in the Electronic Design Automation (EDA) industry. In this context, SmartonAI's intelligent platforms, namely the ChatPlugin and OneCommandLine, have showcased immense potential to revolutionize the way designers interact with such software.

The ChatPlugin, with its ability to break down complex queries into manageable tasks and provide tailored learning resources, simplifies the learning curve for users. On the other hand, OneCommandLine optimizes the design process by providing intelligent plugin recommendations based on users' specific needs.

When these two plugins work in tandem, they not only enhance the user experience but also streamline the design process, fostering an environment of efficiency and productivity. This innovative approach effectively democratizes access to complex EDA software and holds the potential to extend to other intricate software systems.


In conclusion, SmartonAI sets a new benchmark in the EDA industry. By harnessing the power of AI and placing users' needs at the forefront, it paves the way for a more inclusive, productive, and interactive design landscape.

## Reference
[1]: "KiCad EDA." KiCad, https://www.kicad.org/. Accessed 25 July 2023.
[2]: Shen, Yongliang, et al. "HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face." arXiv preprint, 2023, https://doi.org/10.48550/arXiv.2303.17580.
[3]: Radford, Alec, et al. "Improving Language Understanding by Generative Pre-training." OpenAI, 2018
[4]: Radford, Alec, et al. "Language Models are Unsupervised Multitask Learners." OpenAI, 2019
[5]: Brown, Tom B., et al. "Language Models are Few-shot Learners." arXiv preprint, 2020, https://arxiv.org/abs/2005.14165.
[6]: Devlin, Jacob, et al. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." arXiv preprint, 2018, https://arxiv.org/abs/1810.04805.
[7]: "EEschema: Schematic Capture." KiCad Documentation, 2023, https://docs.kicad.org/7.0/en/eeschema/eeschema.pdf. Accessed 25 July 2023.
[8]: "Pcbnew: PCB Layout Editor." KiCad Documentation, 2023, https://docs.kicad.org/7.0/en/pcbnew/pcbnew.pdf. Accessed 25 July 2023.

