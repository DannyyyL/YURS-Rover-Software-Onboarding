import URDFViewer from './URDFViewer.jsx';

export default function App() {
  return (
    <main
      className="grid h-[min(78vh,760px)] min-h-[440px] w-[min(78vw,1100px)] grid-rows-[minmax(360px,1fr)_auto_auto] gap-4"
      aria-label="Interactive Rover 3D model"
    >
      <URDFViewer />
    </main>
  );
}
