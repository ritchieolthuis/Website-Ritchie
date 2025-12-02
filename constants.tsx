import { Experience, Project, Skill, SocialLink, Education } from './types';
import { Github, Linkedin, Mail, Twitter, BookOpen, Briefcase, Award } from 'lucide-react';

/* 
  CONFIGURATION:
  The website is now set up to use online images so it works immediately.
  You do NOT need to download or move files.
*/

export const HERO_DATA = {
  name: "Ritchie Olthuis",
  title: "Strategic Innovator & Business Student",
  tagline: "Bridging the gap between commercial strategy, sustainability, and design thinking.",
  location: "Netherlands",
  availableForWork: true,
};

export const ABOUT_DATA = `I am an ambitious Business Administration and Commercial Economics student with a passion for strategic innovation. Currently pursuing a Pre-master at the University of Twente and a Bachelor's at Windesheim, I specialize in Design Thinking and sustainable business modeling.

My approach combines thorough research with creative problem-solving. I thrive on analyzing complex market trends and translating them into actionable strategies that drive economic, ecological, and social value.`;

export const EDUCATION_DATA: Education[] = [
  {
    id: 'e1',
    school: "University of Twente",
    degree: "Pre-master, Business Administration / Bedrijfskunde",
    period: "Feb 2025 - Jul 2025",
    grade: "Gemiddelde: 7.5",
    description: "Focus on Business Management and academic research methodologies."
  },
  {
    id: 'e2',
    school: "Windesheim",
    degree: "Bachelor's degree, Commerciële Economie",
    period: "Sep 2022 - Jul 2026",
    activities: "Minor: Financiële Besluitvorming",
    description: "Developing skills in innovative research, strategic advice, design thinking, and commercial awareness."
  },
  {
    id: 'e3',
    school: "Windesheim",
    degree: "Propedeuse, Commerciële Economie",
    period: "Sep 2022 - Jul 2023",
    grade: "Gemiddelde: 7.5",
    description: "Foundation year completed with distinction."
  }
];

export const EXPERIENCE_DATA: Experience[] = [
  {
    id: '1',
    role: "Research & Development (R&D)",
    company: "Unica Building Services",
    period: "Aug 2023 - Jan 2024",
    location: "Hoevelaken, Gelderland (Hybrid)",
    description: "Conducted in-depth strategic analysis and innovation development. Responsible for identifying SWOT elements, creating confrontation matrices, and developing comprehensive business models focusing on economic, ecological, and social aspects.",
    skills: ["Design Thinking", "SWOT Analysis", "Business Model Canvas", "Strategic Advice"]
  }
];

export const PROJECTS_DATA: Project[] = [
  {
    id: 'p1',
    title: "Vitens: Corporate Entity Strategy",
    description: "Strategic research into the formation of a new organizational entity specifically targeting the large-scale business market (grootzakelijke markt). Analyzed organizational readiness and market fit.",
    technologies: ["Market Analysis", "Org. Structuring", "Strategic Advice"],
    // Image: Modern corporate building with blue sky (matches Vitens branding)
    imageUrl: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2670&auto=format&fit=crop", 
    link: "#",
  },
  {
    id: 'p2',
    title: "Perron038: Factory Next Activation",
    description: "Developed an activation strategy for 'Factory Next' to transform the location into a bustling testing ground. Focused on attracting users to the facility for on-site prototyping and validation.",
    technologies: ["Innovation Ecosystems", "Location Strategy", "Concept Testing"],
    // Image: Industrial Robot Arm (matches Factory Next / High Tech)
    imageUrl: "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2670&auto=format&fit=crop",
    link: "#",
  },
  {
    id: 'p3',
    title: "Unica: Sustainable Business Model",
    description: "Applied Design Thinking to develop a Triple Bottom Line business model (Economic, Ecological, Social). Created Customer Journeys and Personas to inform international market entry.",
    technologies: ["Sustainability (ESG)", "Design Thinking", "Business Model Canvas"],
    // Image: Electrical/Technical installation context (matches Unica)
    imageUrl: "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=2669&auto=format&fit=crop",
    link: "#",
  }
];

export const SKILLS_DATA: Skill[] = [
  {
    category: "Strategic Analysis",
    items: ["SWOT Analysis", "Confrontation Matrix", "Market Entry", "Trend Analysis"]
  },
  {
    category: "Innovation & Design",
    items: ["Design Thinking", "Prototyping", "Customer Journey Mapping", "Persona Development"]
  },
  {
    category: "Business Management",
    items: ["Business Model Canvas", "Financial Decision Making", "Sustainability (ESG)", "Commercial Awareness"]
  },
  {
    category: "Research",
    items: ["Qualitative Research", "Quantitative Research", "Data Analysis", "Reporting"]
  }
];

export const SOCIAL_LINKS: SocialLink[] = [
  { platform: 'LinkedIn', url: 'https://linkedin.com', icon: <Linkedin size={20} /> },
  { platform: 'Email', url: 'mailto:contact@ritchie.dev', icon: <Mail size={20} /> },
];

export const GEMINI_SYSTEM_INSTRUCTION = `
You are an AI Assistant for Ritchie Olthuis's personal portfolio website.
Your goal is to represent Ritchie professionally as a Business Administration and Commercial Economics student.

Here is Ritchie's context:
Name: ${HERO_DATA.name}
Title: ${HERO_DATA.title}
Education: Student at University of Twente (Pre-master) and Windesheim (Bachelor).
Projects: 
1. Vitens: Corporate Entity Strategy for large-scale business market.
2. Perron038: Factory Next Activation and location strategy.
3. Unica: Sustainable Business Model and R&D.

Skills: ${JSON.stringify(SKILLS_DATA)}

Tone: Professional, strategic, intelligent, and ambitious.
Highlight his skills in Design Thinking, Strategy, and Sustainability.
If asked about coding, clarify that his primary focus is Business and Strategy, though he understands the tech landscape.
`;