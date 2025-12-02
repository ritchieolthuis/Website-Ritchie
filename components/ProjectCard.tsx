import React from 'react';
import { Project } from '../types';
import { Github, ArrowUpRight } from 'lucide-react';
import BentoCard from './BentoCard';

interface ProjectCardProps {
  project: Project;
}

const ProjectCard: React.FC<ProjectCardProps> = ({ project }) => {
  return (
    <BentoCard className="flex flex-col h-full">
      {/* Image Section */}
      <div className="aspect-[16/9] w-full overflow-hidden border-b border-zinc-800 relative group-hover:border-zinc-700 transition-colors">
        <img 
          src={project.imageUrl} 
          alt={project.title} 
          className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 opacity-70 group-hover:opacity-100" 
        />
        {/* Hover Overlay */}
        <div className="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-4">
           <a 
              href={project.link} 
              className="p-3 bg-accent text-black rounded-full transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 hover:scale-110"
              target="_blank" 
              rel="noopener noreferrer"
            >
              <ArrowUpRight size={24} />
            </a>
            {project.github && (
              <a 
                href={project.github} 
                className="p-3 bg-white text-black rounded-full transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-75 hover:scale-110"
                target="_blank" 
                rel="noopener noreferrer"
              >
                <Github size={24} />
              </a>
            )}
        </div>
      </div>

      {/* Content Section */}
      <div className="p-6 flex flex-col flex-grow">
        <div className="flex justify-between items-start mb-3">
          <h3 className="text-xl font-bold text-white font-display uppercase tracking-tight group-hover:text-accent transition-colors">
            {project.title}
          </h3>
        </div>
        
        <p className="text-zinc-400 text-sm leading-relaxed mb-6 flex-grow">
          {project.description}
        </p>

        {/* Tags */}
        <div className="flex flex-wrap gap-2 mt-auto">
          {project.technologies.map((tech) => (
            <span 
              key={tech} 
              className="px-3 py-1 text-[10px] uppercase tracking-wider font-bold rounded-full bg-zinc-900 text-zinc-400 border border-zinc-800 group-hover:border-zinc-700 transition-colors"
            >
              {tech}
            </span>
          ))}
        </div>
      </div>
    </BentoCard>
  );
};

export default ProjectCard;