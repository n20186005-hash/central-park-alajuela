'use client';

import { useTranslations, useMessages } from 'next-intl';

export default function BasicInfo() {
  const t = useTranslations('basicInfo');
  const messages = useMessages() as any;
  const items = messages?.basicInfo?.items || [];

  return (
    <section className="section-padding" style={{ background: 'var(--bg-secondary)' }}>
      <div className="max-w-5xl mx-auto">
        <h2
          className="font-display text-3xl sm:text-4xl font-semibold mb-6"
          style={{ color: 'var(--text-primary)' }}
        >
          {t('title')}
        </h2>
        <div className="w-12 h-0.5 mb-10" style={{ background: 'var(--accent)' }} />

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {items.map((item: any, i: number) => (
            <InfoCard key={i} icon={item.icon} label={item.label} value={item.value} />
          ))}
        </div>
      </div>
    </section>
  );
}

function InfoCard({ icon, label, value }: { icon: string; label: string; value: string }) {
  const getIcon = () => {
    switch (icon) {
      case 'time':
        return '🕒';
      case 'location':
        return '📍';
      case 'airport':
        return '✈️';
      case 'feature':
        return '🌳';
      default:
        return '📌';
    }
  };

  return (
    <div
      className="rounded-xl p-6 flex items-start gap-4"
      style={{ background: 'var(--bg-tertiary)', border: '1px solid var(--border-color)' }}
    >
      <div className="text-3xl leading-none">{getIcon()}</div>
      <div>
        <p className="text-sm mb-1 font-semibold" style={{ color: 'var(--text-muted)' }}>{label}</p>
        <p className="font-medium text-lg leading-snug" style={{ color: 'var(--text-primary)' }}>{value}</p>
      </div>
    </div>
  );
}
