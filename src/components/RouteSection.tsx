'use client';

import { useTranslations, useMessages } from 'next-intl';

export default function RouteSection() {
  const t = useTranslations('route');
  const messages = useMessages() as any;
  const stepsData = (messages?.route?.steps || []) as any[];
  const supplementsData = (messages?.route?.supplements || []) as string[];

  const supplements = Array.from({ length: supplementsData.length }, (_, i) => i);

  return (
    <section className="section-padding" style={{ background: 'var(--bg-secondary)' }}>
      <div className="max-w-4xl mx-auto">
        <h2
          className="font-display text-3xl sm:text-4xl font-semibold mb-6"
          style={{ color: 'var(--text-primary)' }}
        >
          {t('title')}
        </h2>
        <div className="w-12 h-0.5 mb-8" style={{ background: 'var(--accent)' }} />

        <p className="text-lg leading-relaxed mb-10" style={{ color: 'var(--text-secondary)' }}>
          {t('overview')}
        </p>

        <div className="relative mb-10">
          {/* Timeline line */}
          <div
            className="absolute left-6 top-0 bottom-0 w-0.5"
            style={{ background: 'var(--border-color)' }}
          />

          <div className="space-y-6">
            {stepsData.map((stepData: any, index: number) => (
              <RouteStep
                key={index}
                time={stepData.time}
                icon={stepData.icon}
                description={stepData.description}
              />
            ))}
          </div>
        </div>

        {/* Supplements */}
        <div
          className="rounded-xl p-6"
          style={{ background: 'var(--bg-tertiary)', border: '1px solid var(--accent)' }}
        >
          <h3 className="font-display text-xl font-semibold mb-4" style={{ color: 'var(--text-primary)' }}>
            {t('supplementsTitle')}
          </h3>
          <ul className="space-y-3">
            {supplements.map((i) => (
              <li key={i} className="flex items-start gap-3">
                <span className="mt-1.5 flex-shrink-0 w-1.5 h-1.5 rounded-full" style={{ background: 'var(--accent)' }} />
                <span style={{ color: 'var(--text-secondary)' }}>{t(`supplements.${i}` as any)}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}

function RouteStep({ time, icon, description }: { time: string; icon: string; description: string }) {
  return (
    <div className="relative flex gap-4 pl-4">
      {/* Timeline dot */}
      <div
        className="absolute left-4 -translate-x-1/2 w-4 h-4 rounded-full border-2 flex-shrink-0"
        style={{
          background: 'var(--accent)',
          borderColor: 'var(--accent)',
          top: '0.25rem',
        }}
      />

      {/* Time & Icon badge */}
      <div
        className="flex-shrink-0 w-12 h-12 rounded-full flex items-center justify-center text-lg"
        style={{ background: 'var(--accent)', color: 'white' }}
      >
        {icon}
      </div>

      {/* Content */}
      <div
        className="flex-1 rounded-xl p-4"
        style={{ background: 'var(--bg-tertiary)', border: '1px solid var(--border-color)' }}
      >
        <p className="text-sm font-semibold mb-1" style={{ color: 'var(--accent)' }}>
          {time}
        </p>
        <p className="text-sm leading-relaxed" style={{ color: 'var(--text-secondary)' }}>
          {description}
        </p>
      </div>
    </div>
  );
}
