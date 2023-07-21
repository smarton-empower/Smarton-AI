# New Interaction Paradigm for Complex EDA Software Leveraging GPT

## Abstract

In the rapidly evolving field of electronic design automation (EDA), intricate software like KiCad provide extensive design functionalities. However, the intricate command structure and high learning curve create a barrier to entry, particularly for novice printed circuit board (PCB) designers. This results in difficulty in selecting appropriate functions or plugins for varying design purposes, compounded by the lack of intuitive learning methods beyond traditional documentation, videos, and online forums.

To address this challenge, we introduce SmartonAI, an artificial intelligence (AI) interaction helper plugin for KiCad. SmartonAI is inspired by the HuggingGPT framework and employs large language models, such as ChatGPT, to facilitate task planning and execution. On receiving a designer request, SmartonAI conducts a task breakdown and efficiently executes relevant subtasks, such as analysis of help documentation paragraphs and execution of different plugins, along with leveraging the built-in schematic and PCB manipulation functions in KiCad.

Our preliminary results demonstrate that SmartonAI can significantly streamline the PCB design process by simplifying complex commands into intuitive language-based interactions. By harnessing the powerful language capabilities of ChatGPT and the rich design functions of KiCad, the plugin effectively bridges the gap between complex EDA software and user-friendly interaction.

In conclusion, SmartonAI not only has the potential to democratize access to EDA software for novices, but also promises to enhance productivity for experienced designers. Its application could extend to other complex software systems, illustrating the immense potential of AI-assisted user interfaces in advancing digital interactions across various domains.

## 1. Introduction and Overview of SmartonAI
### 1.1. Brief description of SmartonAI

### 1.2. Explanation of the need for such an AI-assisted interface

### 1.3. Overview of the two main components of SmartonAI: Chat Plugin and OneCommandLine Plugin

### 1.4 Support languages

## 2. The Chat Plugin in SmartonAI
### 2.1. Detailed explanation of the Chat Plugin

### 2.2. Description of how it divides common queries and requirements into 20 main tasks and hundreds of subtasks based on KiCad's official documentation

### 2.3. Explanation of how it provides user-specific introductory paragraphs and chat support services based on these tasks and subtasks

### 2.4. Description of how it can add additional information based on user feedback

## 3. The OneCommandLine Plugin in SmartonAI
### 3.1. Detailed explanation of the OneCommandLine Plugin

### 3.2. Description of how it recommends plugins based on user needs

### 3.3. Explanation of how it accepts user input to intelligently call plugins

## 4. The Interaction Between the Chat Plugin and OneCommandLine Plugin
### 4.1. Discussion of how the two plugins work together

### 4.2. Illustration of how they enhance user interaction with KiCad

## 5. Potential Impact and Future Applications
### 5.1. Discussion of the potential of SmartonAI to democratize access to EDA software

### 5.2. Description of how SmartonAI can potentially enhance productivity for experienced designers

### 5.3. Discussion of the possible extension of this approach to other complex software systems
