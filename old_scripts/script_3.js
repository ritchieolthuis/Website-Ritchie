
                window.showSemesterPage = function(pageId) {
                    const evidence = document.getElementById('portfolio-semester-evidence');
                    const pagesContainer = document.getElementById('portfolio-semester-pages');
                    if (evidence && pagesContainer) {
                        evidence.classList.add('hidden');
                        pagesContainer.classList.remove('hidden');
                        document.querySelectorAll('.semester-page').forEach(el => el.classList.add('hidden'));
                        const page = document.getElementById('page-' + pageId);
                        if (page) {
                            page.classList.remove('hidden');
                        }
                        window.scrollTo({ top: 0, behavior: 'smooth' });
                        if (window.lucide) {
                            window.lucide.createIcons();
                        }
                    }
                };
                window.hideSemesterPages = function() {
                    const evidence = document.getElementById('portfolio-semester-evidence');
                    const pagesContainer = document.getElementById('portfolio-semester-pages');
                    if (evidence && pagesContainer) {
                        evidence.classList.remove('hidden');
                        pagesContainer.classList.add('hidden');
                        window.scrollTo({ top: 0, behavior: 'smooth' });
                    }
                };
            