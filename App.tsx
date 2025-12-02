import React, { useState, useEffect } from 'react';
import { 
  ArrowDown, MapPin, Download, ExternalLink, GraduationCap, Briefcase, 
  BookOpen, ArrowUpRight, Mail, Linkedin, Globe, Cpu, Calendar
} from 'lucide-react';
import { HERO_DATA, ABOUT_DATA, EXPERIENCE_DATA, EDUCATION_DATA, PROJECTS_DATA, SKILLS_DATA, SOCIAL_LINKS } from './constants';
import ProjectCard from './components/ProjectCard';
import ChatWidget from './components/ChatWidget';
import BentoCard from './components/BentoCard';

function App() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-background text-primary selection:bg-accent selection:text-black font-sans bg-grid-pattern pb-20">
      
      {/* Top Navigation Bar - Floating Pill */}
      <div className="fixed top-6 left-0 right-0 z-50 flex justify-center pointer-events-none px-4">
        <nav className="pointer-events-auto bg-[#121212]/80 backdrop-blur-xl border border-white/10 rounded-full px-2 py-2 flex items-center gap-1 shadow-2xl">
          <button 
            onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
            className="w-10 h-10 rounded-full bg-zinc-900 flex items-center justify-center text-white font-serif italic border border-zinc-800 hover:border-accent transition-colors"
          >
            R
          </button>
          
          <div className="hidden sm:flex items-center px-2">
            {['About', 'Education', 'Experience', 'Projects'].map((item) => (
              <button
                key={item}
                onClick={() => scrollToSection(item.toLowerCase())}
                className="px-4 py-2 text-sm font-medium text-zinc-400 hover:text-white transition-colors"
              >
                {item}
              </button>
            ))}
          </div>

          <button 
            onClick={() => scrollToSection('contact')}
            className="px-5 py-2.5 bg-white text-black text-sm font-bold rounded-full hover:bg-accent transition-colors flex items-center gap-2"
          >
            <Mail size={16} />
            <span className="hidden sm:inline">Contact</span>
          </button>
        </nav>
      </div>

      <div className="max-w-[1400px] mx-auto pt-24 md:pt-32 px-4 md:px-8">
        
        {/* HERO BENTO GRID */}
        <div className="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-6 gap-4 mb-4">
          
          {/* 1. Name & Title Block (Large) */}
          <BentoCard className="col-span-1 md:col-span-4 lg:col-span-4 row-span-2 p-6 md:p-10 flex flex-col justify-between">
            <div className="absolute top-0 right-0 p-32 bg-accent/5 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none transition-all duration-700 group-hover:bg-accent/10"></div>
            
            <div className="relative z-10">
              <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-900/80 border border-zinc-800 text-[10px] md:text-xs font-mono uppercase tracking-widest text-accent mb-6">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-accent opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-accent"></span>
                </span>
                Available for work
              </div>
              
              <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold font-display uppercase leading-[0.9] tracking-tighter mb-4">
                Ritchie <br />
                <span className="text-zinc-500 transition-colors group-hover:text-zinc-300">Olthuis.</span>
              </h1>
            </div>

            <div className="relative z-10 max-w-xl">
               <h2 className="text-xl md:text-2xl text-white mb-4 font-medium">{HERO_DATA.title}</h2>
               <p className="text-zinc-400 leading-relaxed text-sm md:text-base mb-8 group-hover:text-zinc-300 transition-colors">
                 {HERO_DATA.tagline}
               </p>
               
               <div className="flex flex-wrap gap-3">
                 <button 
                  onClick={() => scrollToSection('projects')}
                  className="px-6 py-3 bg-white text-black font-bold rounded-full hover:bg-accent transition-colors flex items-center gap-2 text-sm z-20 relative"
                 >
                   View Work <ArrowDown size={16} />
                 </button>
                 <button className="px-6 py-3 bg-transparent border border-zinc-700 text-white font-bold rounded-full hover:bg-zinc-800 transition-colors flex items-center gap-2 text-sm z-20 relative">
                   Download CV <Download size={16} />
                 </button>
               </div>
            </div>
          </BentoCard>

          {/* 2. Photo / Avatar Block */}
          <BentoCard className="col-span-1 md:col-span-2 lg:col-span-2 row-span-2 min-h-[300px]">
            <img 
              src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=2574&auto=format&fit=crop" 
              alt="Ritchie Olthuis" 
              className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100"
            />
             <div className="absolute inset-0 bg-gradient-to-t from-[#121212] via-transparent to-transparent opacity-80 pointer-events-none"></div>
             <div className="absolute bottom-6 left-6 pointer-events-none">
               <div className="text-accent font-mono text-xs mb-1">BASED IN</div>
               <div className="text-white font-display font-bold text-xl flex items-center gap-2">
                 <MapPin size={18} /> Netherlands
               </div>
             </div>
          </BentoCard>

          {/* 3. About Stats Block */}
          <BentoCard className="col-span-1 md:col-span-2 lg:col-span-2 p-6 flex flex-col justify-center gap-4 bg-[#151515]">
             <div className="flex justify-between items-center border-b border-zinc-800 pb-4 group-hover:border-zinc-700 transition-colors">
                <span className="text-zinc-500 text-sm uppercase font-mono">Education</span>
                <span className="text-white font-bold">University of Twente</span>
             </div>
             <div className="flex justify-between items-center border-b border-zinc-800 pb-4 group-hover:border-zinc-700 transition-colors">
                <span className="text-zinc-500 text-sm uppercase font-mono">Degree</span>
                <span className="text-white font-bold">Pre-master BA</span>
             </div>
             <div className="flex justify-between items-center">
                <span className="text-zinc-500 text-sm uppercase font-mono">Avg. Grade</span>
                <span className="text-accent font-bold text-lg">7.5</span>
             </div>
          </BentoCard>

           {/* 4. Social Links Block */}
           <BentoCard className="col-span-1 md:col-span-2 lg:col-span-2 p-6 flex items-center justify-between">
              <div className="flex gap-2 z-20">
                 {SOCIAL_LINKS.map((link, i) => (
                  <a 
                    key={i} 
                    href={link.url} 
                    target="_blank" 
                    rel="noopener noreferrer" 
                    className="w-12 h-12 rounded-full bg-zinc-900 border border-zinc-800 flex items-center justify-center text-zinc-400 hover:text-black hover:bg-accent hover:border-accent transition-all duration-300 relative"
                  >
                    {link.icon}
                  </a>
                 ))}
              </div>
              <div className="text-right">
                <div className="text-xs text-zinc-500 font-mono uppercase mb-1">Let's Connect</div>
                <div className="text-white font-bold">Social Profiles</div>
              </div>
           </BentoCard>
           
           {/* 5. Ticker / Marquee Block */}
           <BentoCard className="col-span-1 md:col-span-4 lg:col-span-2 p-6 flex items-center bg-accent text-black" noHover>
              <div className="whitespace-nowrap animate-[slideUp_10s_linear_infinite] font-display font-bold text-lg uppercase tracking-wider flex gap-8">
                 <span>Strategic Innovation</span>
                 <span>•</span>
                 <span>Design Thinking</span>
                 <span>•</span>
                 <span>Sustainability</span>
                 <span>•</span>
                 <span>Business Modeling</span>
              </div>
           </BentoCard>

        </div>

        {/* --- MAIN CONTENT GRID --- */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
          
          {/* LEFT COLUMN: About & Skills */}
          <div className="lg:col-span-1 flex flex-col gap-4">
            
            {/* About Card */}
            <BentoCard id="about" className="p-8">
              <div className="w-10 h-10 rounded-full bg-zinc-900 flex items-center justify-center text-accent mb-6 border border-zinc-800 group-hover:scale-110 transition-transform">
                <Cpu size={20} />
              </div>
              <h3 className="text-2xl font-display font-bold text-white mb-4 uppercase">About</h3>
              <p className="text-zinc-400 text-sm leading-7 mb-6">
                {ABOUT_DATA}
              </p>
              <div className="h-px w-full bg-zinc-800 mb-6 group-hover:bg-zinc-700 transition-colors"></div>
              <div className="flex flex-wrap gap-2">
                {['Innovation', 'Research', 'Strategy', 'ESG'].map(tag => (
                  <span key={tag} className="px-3 py-1 bg-zinc-900 rounded text-xs text-zinc-300 border border-zinc-800">
                    #{tag}
                  </span>
                ))}
              </div>
            </BentoCard>

            {/* Skills Card */}
            <BentoCard id="skills" className="p-8">
              <h3 className="text-xl font-display font-bold text-white mb-6 uppercase flex items-center gap-2">
                <span className="w-2 h-2 bg-accent rounded-full animate-pulse"></span>
                Expertise
              </h3>
              <div className="space-y-6 relative z-10">
                {SKILLS_DATA.slice(0, 3).map((category) => (
                  <div key={category.category}>
                    <h4 className="text-xs font-mono uppercase text-zinc-500 mb-3">{category.category}</h4>
                    <div className="flex flex-wrap gap-2">
                      {category.items.map((item) => (
                        <span key={item} className="px-2 py-1 text-xs font-medium text-white bg-zinc-800/50 border border-zinc-700 rounded hover:border-accent hover:text-accent transition-colors cursor-default">
                          {item}
                        </span>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </BentoCard>

          </div>

          {/* MIDDLE & RIGHT COLUMN: Education, Experience, Projects */}
          <div className="lg:col-span-2 flex flex-col gap-4">
            
            {/* Education Section */}
            <BentoCard id="education" className="p-8">
               <div className="flex items-center justify-between mb-8">
                 <h3 className="text-2xl font-display font-bold text-white uppercase">Education</h3>
                 <GraduationCap className="text-zinc-600 group-hover:text-white transition-colors" />
               </div>
               
               <div className="space-y-8">
                 {EDUCATION_DATA.map((edu, index) => (
                   <div key={edu.id} className="relative pl-8 border-l border-zinc-800 group-hover:border-zinc-700 transition-colors">
                      <div className={`absolute left-[-5px] top-1 w-2.5 h-2.5 rounded-full ${index === 0 ? 'bg-accent' : 'bg-zinc-700'}`}></div>
                      <div className="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-2 mb-2">
                        <h4 className="text-lg font-bold text-white">{edu.school}</h4>
                        <span className="text-xs font-mono text-zinc-500 bg-zinc-900 px-2 py-1 rounded border border-zinc-800">
                          {edu.period}
                        </span>
                      </div>
                      <div className="text-sm text-zinc-400 mb-2 font-medium">{edu.degree}</div>
                      {edu.description && <p className="text-sm text-zinc-500 leading-relaxed max-w-2xl">{edu.description}</p>}
                      {edu.grade && <div className="mt-3 text-xs font-bold text-accent">{edu.grade}</div>}
                   </div>
                 ))}
               </div>
            </BentoCard>

            {/* Experience Section */}
            <BentoCard id="experience" className="p-8 bg-[#151515]">
               <div className="flex items-center justify-between mb-8">
                 <h3 className="text-2xl font-display font-bold text-white uppercase">Experience</h3>
                 <Briefcase className="text-zinc-600 group-hover:text-white transition-colors" />
               </div>

               <div className="space-y-6">
                 {EXPERIENCE_DATA.map((exp) => (
                   <div key={exp.id} className="group/item">
                      <div className="flex flex-col md:flex-row md:items-center justify-between gap-2 mb-4">
                        <div>
                          <h4 className="text-xl font-bold text-white group-hover/item:text-accent transition-colors">{exp.role}</h4>
                          <div className="text-zinc-400 text-sm">{exp.company} • {exp.location}</div>
                        </div>
                        <span className="text-xs font-mono text-zinc-500 border border-zinc-800 px-3 py-1 rounded-full">
                          {exp.period}
                        </span>
                      </div>
                      <p className="text-zinc-400 text-sm leading-relaxed mb-4 whitespace-pre-line border-l-2 border-zinc-800 pl-4 group-hover/item:border-accent transition-colors">
                        {exp.description}
                      </p>
                      <div className="flex flex-wrap gap-2">
                         {exp.skills.map(skill => (
                           <span key={skill} className="text-[10px] uppercase font-bold text-zinc-500 bg-zinc-900 px-2 py-1 rounded">
                             {skill}
                           </span>
                         ))}
                      </div>
                   </div>
                 ))}
               </div>
            </BentoCard>

            {/* Projects Grid */}
            <div id="projects" className="grid grid-cols-1 md:grid-cols-2 gap-4">
               <div className="md:col-span-2 flex items-center justify-between py-4">
                  <h3 className="text-2xl font-display font-bold text-white uppercase">Selected Projects</h3>
                  <a href="#" className="text-xs font-mono text-zinc-500 hover:text-white flex items-center gap-1 transition-colors">
                    VIEW ALL <ArrowUpRight size={12} />
                  </a>
               </div>
               {PROJECTS_DATA.map((project) => (
                 <div key={project.id} className="h-full">
                   <ProjectCard project={project} />
                 </div>
               ))}
            </div>

          </div>
        </div>

        {/* Contact Footer Block */}
        <div id="contact" className="mt-4 mb-8">
          <BentoCard className="p-10 md:p-20 text-center">
             <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-accent to-transparent opacity-50"></div>
             
             <div className="relative z-10">
               <h2 className="text-4xl md:text-6xl font-display font-bold text-white uppercase mb-6 tracking-tight">
                 Let's work <span className="text-zinc-600 transition-colors group-hover:text-zinc-400">Together</span>
               </h2>
               <p className="text-zinc-400 max-w-xl mx-auto mb-10 text-lg">
                 Open to discussing new opportunities, strategic collaborations, or sustainability initiatives.
               </p>
               
               <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
                 <a 
                   href="mailto:contact@ritchie.dev"
                   className="px-8 py-4 bg-accent text-black font-bold rounded-full hover:bg-[#b3e600] transition-colors min-w-[200px]"
                 >
                   Send Email
                 </a>
                 <a 
                   href="#" 
                   className="px-8 py-4 bg-white text-black font-bold rounded-full hover:bg-zinc-200 transition-colors min-w-[200px] flex items-center justify-center gap-2"
                 >
                   <Calendar size={18} />
                   Schedule Call
                 </a>
                 <a 
                   href="https://linkedin.com"
                   target="_blank"
                   rel="noopener noreferrer"
                   className="px-8 py-4 bg-zinc-900 text-white font-bold rounded-full border border-zinc-800 hover:border-zinc-600 transition-colors min-w-[200px] flex items-center justify-center gap-2"
                 >
                   <Linkedin size={18} />
                   LinkedIn
                 </a>
               </div>

               <div className="mt-20 pt-10 border-t border-zinc-800 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-zinc-600 font-mono uppercase">
                 <span>© {new Date().getFullYear()} Ritchie Olthuis</span>
                 <div className="flex gap-6">
                   <a href="#" className="hover:text-zinc-400">Privacy</a>
                   <a href="#" className="hover:text-zinc-400">Terms</a>
                   <a href="#" className="hover:text-zinc-400">Sitemap</a>
                 </div>
               </div>
             </div>
          </BentoCard>
        </div>

      </div>

      <ChatWidget />
    </div>
  );
}

export default App;