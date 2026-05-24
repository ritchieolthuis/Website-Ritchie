import React, { useState } from 'react';
import { PAGES, STUDY_YEARS } from './constants';

export default function App() {
  const [activePage, setActivePage] = useState<string>('intro');
  const [activeYear, setActiveYear] = useState<string | null>(null);

  const navigationItems = Object.keys(PAGES).map(key => ({ key, label: PAGES[key as keyof typeof PAGES].title }));

  const renderContent = () => {
    if (activePage === 'bewijsstukken' && activeYear) {
      const year = STUDY_YEARS[activeYear as keyof typeof STUDY_YEARS];
      return (
        <div className="max-w-3xl mx-auto">
          <button onClick={() => setActiveYear(null)} className="mb-8 text-lime-400 hover:text-white transition-colors">← Terug naar Portfolio / Back to Portfolio</button>
          <h1 className="text-3xl font-bold mb-6 text-lime-400">{year.title}</h1>
        </div>
      );
    }
    if (activePage === 'bewijsstukken') {
      return (
        <div className="max-w-4xl mx-auto">
          <h1 className="text-4xl font-bold mb-12 text-white">BEWIJSSTUKKEN & PORTFOLIO</h1>
          <div className="flex flex-col gap-4">
            {Object.entries(STUDY_YEARS).map(([key, year]) => (
              <button 
                key={key} 
                onClick={() => setActiveYear(key)} 
                className="w-full text-left p-6 rounded-xl bg-neutral-900 border border-neutral-800 hover:border-lime-500 transition-all text-xl font-bold text-white hover:text-lime-400"
              >
                {year.title}
              </button>
            ))}
          </div>
        </div>
      );
    }
    const page = PAGES[activePage as keyof typeof PAGES];
    return (
      <div className="max-w-3xl mx-auto">
        <h1 className="text-4xl font-bold mb-6 text-white">{page.title}</h1>
        <div className="prose prose-invert prose-lime">
          <p className="text-neutral-300 leading-relaxed">{page.content}</p>
        </div>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-100">
      <nav className="p-6 flex items-center justify-between border-b border-neutral-800">
        <div className="font-bold text-xl uppercase tracking-widest">R</div>
        <div className="flex gap-4 flex-wrap">
          {navigationItems.map(item => (
            <button key={item.key} onClick={() => { setActivePage(item.key); setActiveYear(null); }} className={`px-4 py-2 rounded-full font-medium ${activePage === item.key ? 'bg-lime-400 text-neutral-950' : 'text-neutral-400 hover:text-white'}`}>
              {item.label}
            </button>
          ))}
        </div>
        <div className="flex gap-4">
          <button className="text-neutral-400">EN</button>
          <button className="bg-neutral-800 px-6 py-2 rounded-full">Contact</button>
        </div>
      </nav>
      <main className="p-8">
        {renderContent()}
      </main>
    </div>
  );
}
