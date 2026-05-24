import React from 'react';

interface BentoCardProps {
  title: string;
  description: string;
  onClick: () => void;
}

export default function BentoCard({ title, description, onClick }: BentoCardProps) {
  return (
    <button
      onClick={onClick}
      className="p-6 rounded-2xl bg-neutral-900 border border-neutral-800 hover:border-lime-500 transition-all text-left group"
    >
      <h3 className="text-xl font-bold mb-2 text-white group-hover:text-lime-400">
        {title}
      </h3>
      <p className="text-neutral-400 text-sm leading-relaxed">
        {description}
      </p>
    </button>
  );
}
